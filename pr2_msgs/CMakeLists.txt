cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
rospack(pr2_msgs)
genmsg()
gensrv()


rospack_add_pyunit_future(test/test_pr2_msgs_migration.py)
