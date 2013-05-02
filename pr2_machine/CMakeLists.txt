cmake_minimum_required(VERSION 2.8.3)
project(pr2_machine)

find_package(catkin REQUIRED )

catkin_package()

install(FILES pr2.machine sim.machine 
   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
