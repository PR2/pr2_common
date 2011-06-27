cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
rosbuild_init()
rosbuild_genmsg()
rosbuild_gensrv()

rosbuild_add_rostest(launch/test_pr2_msgs_migration.launch)
#rosbuild_add_pyunit(test/test_pr2_msgs_migration.py)
