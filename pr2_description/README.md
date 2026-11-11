This package contains the description of the PR2 robot. It supercedes
the older [pr2_defs](pr2_defs) package which was written for the alpha
hardware.

### Package organization

This package contains robot description files for PR2, organized into
subdirectories as follows:

- `urdf/` contains ([xacro](https://index.ros.org/p/xacro)
  representations of) [urdf](https://index.ros.org/p/urdf) descriptions
  of various parts of the PR2 (arm, torso, etc.).
- `robots/` contains ([xacro](https://index.ros.org/p/xacro)
  representations of) [urdf](https://index.ros.org/p/urdf) descriptions
  of the full robot, that refer to the macros in `urdf/`
- `gazebo/` contains ([xacro](https://index.ros.org/p/xacro)
  representations of) [urdf](https://index.ros.org/p/urdf) descriptions
  of simulated PR2 components, like the simulated battery controller.
- `meshes/` contains mesh files (`.stl`,`.dae`) for visualization
  and collision properties.

### Changes from Alpha URDFs

Some notable changes from [pr2_defs](pr2_defs):

- updated `frame_id`: `base_laser` \&rarr; `base_laser_link`
  (consistent with tilt_laser_link)
- new `frame_id`:
  `{narrow,wide}_stereo_{l,r}_stereo_camera_optical_frame`
- removed frame: `plug_holder` (might need to add back for
  plug_in_gazebo to work)

## PR2 Coordinate Frames

To see the PR2 URDF graphically, you can 

```
rosrun xacro xacro `rospack find pr2_description`/robots/pr2.urdf.xacro > pr2.urdf
urdf_to_graphiz pr2.urdf
evince pr2.pdf
```

 A
snapshot (r46956) is attached [here](doc/pr2.pdf) for reference.

In general, PR2 URDF contains a tree structured set of links and joints,
with `base_footprint` as the root link of the tree.

## Working with a Kinect

To use the original Kinect with the PR2 (either robot or simulation),
set the KINECT1 environment variable to true. 

```
export KINECT1=true
```


To use a Kinect2 with the PR2 (either robot or simulation), set the
KINECT2 environment variable to true. 

```
export KINECT2=true
```

 If both
variables are set, the Kinect 2 will take precedence over the original
Kinect.

------------------------------------------------------------------------

[CategoryURDF](CategoryURDF)

## Tutorials

Tutorials on using the [urdf](https://index.ros.org/p/urdf) file format:

- [Adding Physical and Collision Properties to a URDF Model](https://index.ros.org/p/urdf):
  Learn how to add collision and inertial properties to links, and how
  to add joint dynamics to joints.
- [Adding a Sensor to the PR2 URDF](https://index.ros.org/p/urdf): This
  tutorial describes how to add a camera sensor to the PR2 URDF.
- [Building a Movable Robot Model with URDF](https://index.ros.org/p/urdf):
  Learn how to define movable joints in URDF
- [Building a Visual Robot Model with URDF from Scratch](https://index.ros.org/p/urdf):
  Learn how to build a visual model of a robot that you can view in Rviz
- [Create your own urdf file](https://index.ros.org/p/urdf): In this
  tutorial you start creating your own urdf robot description file.
- [Parse a urdf file](https://index.ros.org/p/urdf): This tutorial
  teaches you how to use the urdf parser
- [Understanding the PR2 Robot Description](https://index.ros.org/p/urdf):
  This tutorial explains the layout of the top level URDF Xacro file for
  a complex robot such as PR2.
- [Understanding the PR2 URDF description, Part 2](https://index.ros.org/p/urdf):
  Describes one of the low-level components of the PR2 definition in
  full detail.
- [Understanding the PR2 Robot Description Extensions for Gazebo Simulator](https://index.ros.org/p/urdf):
  This tutorial explains URDF extensions used by Gazebo simulation.
- [Using Xacro to Clean Up a URDF File](https://index.ros.org/p/urdf):
  Learn some tricks to reduce the amount of code in a URDF file using
  Xacro
- [Using a URDF in Gazebo](https://index.ros.org/p/urdf): Preliminary
  tutorial on how to spawn and control your robot in Gazebo.
- [Using urdf with robot_state_publisher](https://index.ros.org/p/urdf):
  This tutorial gives a full example of a robot model with URDF that
  uses robot_state_publisher. First, we create the URDF model with all
  the necessary parts. Then we write a node which publishes the
  JointState and transforms. Finally, we run all the parts together.

Using URDF with [kdl_parser](https://index.ros.org/p/kdl_parser)

- [Start using the KDL parser](https://index.ros.org/p/kdl_parser): This
  tutorial teaches you how to create a KDL Tree from a
  [URDF](https://index.ros.org/p/urdf) file
