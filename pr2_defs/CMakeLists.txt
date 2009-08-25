
cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
rospack(pr2_defs)

rospack_add_gtest(test_urdf test/test_urdf.cpp)

find_ros_package(pr2_defs)

file(GLOB def_files ${CMAKE_CURRENT_SOURCE_DIR}/defs/*.xml)

# xacro file generation
find_ros_package(xacro)
find_ros_package(ivcon)
find_ros_package(convex_decomposition)

set(pr2_robot_files "")

#TODO: following files are needed by openrave
# iterate through all the robot/*.xacro.xml files and generate *.mesh and *.iv files
file(GLOB urdf_def_files ${CMAKE_CURRENT_SOURCE_DIR}/defs/*/*.xacro)
file(GLOB robot_urdf_files ${CMAKE_CURRENT_SOURCE_DIR}/robots/*.urdf.xacro)

foreach(it ${robot_urdf_files})
  get_filename_component(basepath ${it} PATH)
  get_filename_component(basename ${it} NAME_WE)

  message(" processing robot urdf file :",${basepath}," : ",${basename})

  set(expanded_file "${basepath}/${basename}.urdf")
  message("    produce expanded file :",${expanded_file})

  add_custom_command(
    OUTPUT ${expanded_file}
    COMMAND ${xacro_PACKAGE_PATH}/xacro.py
    ARGS ${it} > ${expanded_file}
    DEPENDS ${it} ${urdf_def_files})

  set(pr2_robot_files ${pr2_robot_files} ${expanded_file})
endforeach(it)


#TODO: following files are needed by openrave
# iterate through all the robot/*.xacro.xml files and generate *.mesh and *.iv files
file(GLOB robot_xacro_files ${CMAKE_CURRENT_SOURCE_DIR}/robots/*.xacro.xml)

foreach(it ${robot_xacro_files})
  get_filename_component(basepath ${it} PATH)
  get_filename_component(basename ${it} NAME_WE)

  message(" processing robot xacro file :",${basepath}," : ",${basename})

  set(expanded_file "${basepath}/${basename}.expanded.xml")
  message("    produce expanded file :",${expanded_file})

  add_custom_command(
    OUTPUT ${expanded_file}
    COMMAND ${xacro_PACKAGE_PATH}/xacro.py
    ARGS ${it} > ${expanded_file}
    DEPENDS ${it} ${def_files})

  set(pr2_robot_files ${pr2_robot_files} ${expanded_file})
endforeach(it)







#iv files
# iterate through all the stl files and generate *.mesh and *.iv files
file(GLOB pr2_stl_files ${CMAKE_CURRENT_SOURCE_DIR}/meshes/*.stl)
set(pr2_gen_files "")

foreach(it ${pr2_stl_files})
  get_filename_component(basepath ${it} PATH)
  get_filename_component(basename ${it} NAME_WE)

  IF ( ${basename} MATCHES "_convex" )

    message("ignoring stale .._convex.stl file:",${basename})

  ELSE ( ${basename} MATCHES "_convex" )

    #convex decomposition obj files
    add_custom_command(
      OUTPUT ${basepath}/convex
      # CMake 2.4 doesn't offer the make_directory command.
      #COMMAND ${CMAKE_COMMAND} -E make_directory
      COMMAND mkdir -p
      ARGS ${basepath}/convex)

    #create obj files for convex decomposition from stl files
    add_custom_command(
      OUTPUT ${basepath}/convex/${basename}.obj
      COMMAND ${ivcon_PACKAGE_PATH}/bin/ivcon
      ARGS ${it} ${basepath}/convex/${basename}.obj
      DEPENDS ${it} ${basepath}/convex)

    set(pr2_gen_files ${pr2_gen_files} ${basepath}/convex/${basename}.obj)

    add_custom_command(
      OUTPUT ${basepath}/convex/${basename}_convex.obj
      COMMAND ${convex_decomposition_PACKAGE_PATH}/convex_decomposition/bin/convex_decomposition
      ARGS ${basepath}/convex/${basename}.obj -v12 -p10
      DEPENDS ${basepath}/convex/${basename}.obj ${basepath}/convex)

    set(pr2_gen_files ${pr2_gen_files} ${basepath}/convex/${basename}_convex.obj)

    #convert obj files back to stlb, put in directory named convex
    add_custom_command(
      OUTPUT ${basepath}/convex/${basename}_convex.stlb
      COMMAND ${ivcon_PACKAGE_PATH}/bin/ivcon
      ARGS ${basepath}/convex/${basename}_convex.obj ${basepath}/convex/${basename}_convex.stlb
      DEPENDS ${it} ${basepath}/convex ${basepath}/convex/${basename}_convex.obj)

    set(pr2_gen_files ${pr2_gen_files} ${basepath}/convex/${basename}_convex.stlb)

    #convert obj files back to stla, put in directory named convex
    add_custom_command(
      OUTPUT ${basepath}/convex/${basename}_convex.stla
      COMMAND ${ivcon_PACKAGE_PATH}/bin/ivcon
      ARGS ${basepath}/convex/${basename}_convex.obj ${basepath}/convex/${basename}_convex.stla
      DEPENDS ${it} ${basepath}/convex ${basepath}/convex/${basename}_convex.obj)

    set(pr2_gen_files ${pr2_gen_files} ${basepath}/convex/${basename}_convex.stla)

    #iv files
    add_custom_command(
      OUTPUT ${basepath}/${basename}.iv
      COMMAND ${ivcon_PACKAGE_PATH}/bin/ivcon
      ARGS ${it} ${basepath}/${basename}.iv
      DEPENDS ${it})
    add_custom_command(
      OUTPUT ${basepath}/convex/${basename}_convex.iv
      COMMAND ${ivcon_PACKAGE_PATH}/bin/ivcon
      ARGS ${basepath}/convex/${basename}_convex.obj ${basepath}/convex/${basename}_convex.iv
      DEPENDS ${it} ${basepath}/convex ${basepath}/convex/${basename}_convex.obj)
     
    set(pr2_gen_files ${pr2_gen_files} ${basepath}/${basename}.iv ${basepath}/convex/${basename}_convex.iv)


  ENDIF ( ${basename} MATCHES "_convex" )

endforeach(it)

add_custom_target(media_files ALL DEPENDS ${pr2urdf} ${pr2robot_expanded} ${prfrobot_expanded} ${prgrobot_expanded} ${pr2prototype1_expanded} ${pr2larm_expanded} ${pr2rarm_expanded} ${pr2lgripper_expanded} ${pr2rgripper_expanded} ${pr2_gen_files} ${pr2_robot_files})

#TODO; stop bin and lib from being generated
