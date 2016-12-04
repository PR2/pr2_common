cmake_minimum_required(VERSION 2.8.3)
project(pr2_msgs)
find_package(catkin REQUIRED COMPONENTS message_generation geometry_msgs)

add_message_files(FILES
  AccelerometerState.msg
  AccessPoint.msg
  BatteryServer.msg
  BatteryServer2.msg
  BatteryState.msg
  BatteryState2.msg
  DashboardState.msg
  GPUStatus.msg
  LaserScannerSignal.msg
  LaserTrajCmd.msg
  PeriodicCmd.msg
  PowerBoardState.msg
  PowerState.msg
  PressureState.msg
)

generate_messages(DEPENDENCIES geometry_msgs)

catkin_package(CATKIN_DEPENDS message_runtime geometry_msgs)

#rosbuild_add_rostest(launch/test_pr2_msgs_migration.launch)
##rosbuild_add_pyunit(test/test_pr2_msgs_migration.py)
