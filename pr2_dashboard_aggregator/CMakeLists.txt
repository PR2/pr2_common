cmake_minimum_required(VERSION 2.8.3)
project(pr2_dashboard_aggregator)

find_package(catkin REQUIRED)

catkin_package()

install(PROGRAMS dashboard_aggregator.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
