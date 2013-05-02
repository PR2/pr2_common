# http://ros.org/doc/groovy/api/catkin/html/user_guide/supposed.html
cmake_minimum_required(VERSION 2.8.3)
project(pr2_description)
find_package(catkin REQUIRED COMPONENTS urdfdom)

# include_directories(include ${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS})

#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)


find_package(Boost REQUIRED COMPONENTS thread)
include_directories(${Boost_INCLUDE_DIRS})

#target_link_libraries(test_urdf ${Boost_LIBRARIES})


# mesh file generations
# iterate through all the stl files to:
#  1. convert to *.iv files
#  2. generate convex decomposed .stl

file(GLOB pr2_stl_files ${CMAKE_CURRENT_SOURCE_DIR}/meshes/*/*.stl)
set(pr2_gen_files "")

foreach(it ${pr2_stl_files})
  get_filename_component(basepath ${it} PATH)
  get_filename_component(basename ${it} NAME_WE)

  IF ( ${basename} MATCHES "_convex" )

    message("ignoring stale .._convex.stl file:",${basename})

  ELSE ( ${basename} MATCHES "_convex" )

    # create subdirectory convex
    add_custom_command(
      OUTPUT ${basepath}/convex
      # CMake 2.4 doesn't offer the make_directory command.
      #COMMAND ${CMAKE_COMMAND} -E make_directory
      COMMAND mkdir -p
      ARGS ${basepath}/convex)

    # create subdirectory iv
    add_custom_command(
      OUTPUT ${basepath}/iv
      # CMake 2.4 doesn't offer the make_directory command.
      #COMMAND ${CMAKE_COMMAND} -E make_directory
      COMMAND mkdir -p
      ARGS ${basepath}/iv)

    #create obj files for convex decomposition from stl files
    add_custom_command(
      OUTPUT ${basepath}/convex/${basename}.obj
      COMMAND ivcon
      ARGS ${it} ${basepath}/convex/${basename}.obj
      DEPENDS ${it} ${basepath}/convex)

    set(pr2_gen_files ${pr2_gen_files} ${basepath}/convex/${basename}.obj)

    #convex decompose object files
    add_custom_command(
      OUTPUT ${basepath}/convex/${basename}_convex.obj
      COMMAND convex_decomposition
      ARGS ${basepath}/convex/${basename}.obj -v12 -p10
      DEPENDS ${basepath}/convex/${basename}.obj ${basepath}/convex)

    set(pr2_gen_files ${pr2_gen_files} ${basepath}/convex/${basename}_convex.obj)

    #convert obj files back to stlb, put in directory named convex
    add_custom_command(
      OUTPUT ${basepath}/convex/${basename}_convex.stlb
      COMMAND ivcon
      ARGS ${basepath}/convex/${basename}_convex.obj ${basepath}/convex/${basename}_convex.stlb
      DEPENDS ${it} ${basepath}/convex ${basepath}/convex/${basename}_convex.obj)

    set(pr2_gen_files ${pr2_gen_files} ${basepath}/convex/${basename}_convex.stlb)

    #convert obj files back to stla, put in directory named convex
    add_custom_command(
      OUTPUT ${basepath}/convex/${basename}_convex.stla
      COMMAND ivcon
      ARGS ${basepath}/convex/${basename}_convex.obj ${basepath}/convex/${basename}_convex.stla
      DEPENDS ${it} ${basepath}/convex ${basepath}/convex/${basename}_convex.obj)

    set(pr2_gen_files ${pr2_gen_files} ${basepath}/convex/${basename}_convex.stla)

    #create iv files
    add_custom_command(
      OUTPUT ${basepath}/iv/${basename}.iv
      COMMAND ivcon
      ARGS ${it} ${basepath}/iv/${basename}.iv
      DEPENDS ${basepath}/iv ${it})
    add_custom_command(
      OUTPUT ${basepath}/convex/${basename}_convex.iv
      COMMAND ivcon
      ARGS ${basepath}/convex/${basename}_convex.obj ${basepath}/convex/${basename}_convex.iv
      DEPENDS ${it} ${basepath}/convex ${basepath}/convex/${basename}_convex.obj)
     
    set(pr2_gen_files ${pr2_gen_files} ${basepath}/iv/${basename}.iv ${basepath}/convex/${basename}_convex.iv)


  ENDIF ( ${basename} MATCHES "_convex" )

endforeach(it)

add_custom_target(media_files ALL DEPENDS ${pr2urdf} ${pr2robot_expanded} ${prfrobot_expanded} ${prgrobot_expanded} ${pr2prototype1_expanded} ${pr2larm_expanded} ${pr2rarm_expanded} ${pr2lgripper_expanded} ${pr2rgripper_expanded} ${pr2_gen_files} )

# TODO: fill in what other packages will need to use this package
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
    DEPENDS convex_decomposition ivcon urdfdom xacro
    CATKIN-DEPENDS # TODO
    INCLUDE_DIRS # TODO include
    LIBRARIES # TODO
)

catkin_add_gtest(test_urdf test/test_urdf.cpp)
