#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

import roslib
roslib.load_manifest('pr2_msgs')

import sys
import struct

import unittest

import rostest
import rosrecord
import rosbagmigration

import re
from cStringIO import StringIO
import os

import rospy

import math

def repack(x):
  return struct.unpack('<f',struct.pack('<f',x))[0]

class TestPR2MsgsMigration(unittest.TestCase):


# (*) LaserScannerSignal.saved

########### LaserScannerSignal ###############

  def get_old_laser_scanner_signal(self):
    laser_scanner_signal_classes = self.load_saved_classes('pr2_mechanism_controllers_LaserScannerSignal.saved')

    laser_scanner_signal = laser_scanner_signal_classes['pr2_mechanism_controllers/LaserScannerSignal']

    return laser_scanner_signal(None, 123)

  def get_new_laser_scanner_signal(self):
    from pr2_msgs.msg import LaserScannerSignal

    return LaserScannerSignal(None, 123)

  def test_laser_scanner_signal(self):
    self.do_test('laser_scanner_signal', self.get_old_laser_scanner_signal, self.get_new_laser_scanner_signal)


########### Helper functions ###########


  def setUp(self):
    self.pkg_dir = roslib.packages.get_pkg_dir("pr2_msgs")


  def load_saved_classes(self,saved_msg):
    f = open("%s/test/saved/%s"%(self.pkg_dir,saved_msg), 'r')

    type_line = f.readline()
    pat = re.compile(r"\[(.*)]:")
    type_match = pat.match(type_line)

    self.assertTrue(type_match is not None, "Full definition file malformed.  First line should be: '[my_package/my_msg]:'")

    saved_type = type_match.groups()[0]
    saved_full_text = f.read()

    saved_classes = roslib.genpy.generate_dynamic(saved_type,saved_full_text)

    self.assertTrue(saved_classes is not None, "Could not generate class from full definition file.")
    self.assertTrue(saved_classes.has_key(saved_type), "Could not generate class from full definition file.")

    return saved_classes

  def do_test(self, name, old_msg, new_msg):
    # Name the bags
    oldbag = "%s/test/%s_old.bag"%(self.pkg_dir,name)
    newbag = "%s/test/%s_new.bag"%(self.pkg_dir,name)

    # Create an old message
    bag = rosrecord.Rebagger(oldbag)
    bag.add("topic", old_msg(), roslib.rostime.Time())
    bag.close()

    # Check and migrate
    res = rosbagmigration.checkbag(oldbag, [])
    self.assertTrue(res is None or res == [], 'Bag not ready to be migrated')
    res = rosbagmigration.fixbag(oldbag, newbag, [])
    self.assertTrue(res, 'Bag not converted successfully')

    # Pull the first message out of the bag
    msgs = [msg for msg in rosrecord.logplayer(newbag)]

    # Reserialize the new message so that floats get screwed up, etc.
    m = new_msg()
    buff = StringIO()
    m.serialize(buff)
    m.deserialize(buff.getvalue())
    
    #Compare
#    print "old"
#    print roslib.message.strify_message(msgs[0][1])
#    print "new"
#    print roslib.message.strify_message(m)

    # Strifying them helps make the comparison easier until I figure out why the equality operator is failing
    self.assertTrue(roslib.message.strify_message(msgs[0][1]) == roslib.message.strify_message(m))
#    self.assertTrue(msgs[0][1] == m)

    #Cleanup
    os.remove(oldbag)
    os.remove(newbag)


if __name__ == '__main__':
  rostest.unitrun('pr2_msgs', 'test_pr2_msgs_migration', TestPR2MsgsMigration, sys.argv)
