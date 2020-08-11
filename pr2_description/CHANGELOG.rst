^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pr2_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.13.0 (2020-08-11)
-------------------
* Cleanup collision/auxiliary shapes in urdf (`#280 <https://github.com/pr2/pr2_common/issues/280>`_)

  * remove auxiliary shapes from kinect2 links
    If one wants to see the frames, just enable the frame in RViz.
    There is no need whatsoever to keep these in the description.
  * provide bounding box for kinect2 spoiler
    to enable *some* collision checking.
    It was not enabled at all before and it's barely in the workspace of the arms at all (without tool use).
    So a rough bounding box is fine.
  * remove useless visual geometry
    MoveIt master recently changed its policy w.r.t. empty collision geometries.
    The current version complains:
    ros.moveit_core.robot_model.empty_collision_geometry: Link sensor_mount_link has visual geometry but no collision geometry. Collision geometry will be left empty. Fix your URDF file by explicitly specifying collision geometry.
    ros.moveit_core.robot_model.empty_collision_geometry: Link double_stereo_link has visual geometry but no collision geometry. Collision geometry will be left empty. Fix your URDF file by explicitly specifying collision geometry.
    As these visuals are not helpful and do not add anything to the description, I just remove them.
  * remove guessed inertia on base_footprint
    These values are obviously fictitious (the whole link is...)
    Additionally, KDL datastructures have been complaining about this for ages
    because KDL does not support inertials for the model root
    (whatever that means).

* cleanup rviz errors (`#278 <https://github.com/pr2/pr2_common/issues/278>`_)

  * use collada to store kinect mesh
    The STL produced the following warning with RViz:
    [ WARN]: The STL file 'package://pr2_description/meshes/sensors/kinect2_v0/kinect2_assembly.STL' is malformed. It starts with the word 'solid', indicating that it's an ASCII STL file, but it does not contain the word 'endsolid' so it is either a malformed ASCII STL file or it is actually a binary STL file. Trying to interpret it as a binary STL file instead.
  * fix TIFFFieldWithTag errors by converting to png files
    The error seems to stem from a problem in libtiff, so a reasonable
    way to resolve it was to change to a different file format.
    The texture files should not be used in isolation from the corresponding
    dae file, so removing the old tiff files retains API.

* Contributors: Kei Okada, v4hn

1.12.4 (2019-04-24)
-------------------
* Merge pull request `#274 <https://github.com/PR2/pr2_common/issues/274>`_ from knorth55/fix-gripper
  Revert `#255 <https://github.com/PR2/pr2_common/issues/255>`_
* Revert "[pr2_description] fix: gripper reduction 3141.6 -> 314.16"
  This reverts commit d5c8f476c6882b74a03bdc39eccf36823da3ad97.
* Contributors: Kei Okada, Shingo Kitagawa

1.12.3 (2018-09-10)
-------------------
* Merge pull request `#272 <https://github.com/pr2/pr2_common/issues/272>`_ from k-okada/add_travis
  update travis.yml
* ModelInterfaceSharedPtr is only available on newer urdfdom
* fix for urdfmodel 1.0.0 (melodic)
* test_urdf uses rosrun within the code
* Merge pull request `#270 <https://github.com/pr2/pr2_common/issues/270>`_ from TAMS-Group/pr-kinetic-fixed-xmlns
  xmlns should include www
* xmlns should include www
  According to the tutorials:
  http://wiki.ros.org/urdf/Tutorials/Using%20Xacro%20to%20Clean%20Up%20a%20URDF%20File
  xacro complains when some xacro components specify the URL
  as http://www.ros.org/wiki/xacro and others
  as http://ros.org/wiki/xacro.
* Contributors: Kei Okada, v4hn

1.12.2 (2018-04-18)
-------------------
* Merge pull request `#269 <https://github.com/pr2/pr2_common/issues/269>`_ from bmagyar/kinetic-devel
  Fix pr2_description warnings
* Remove playerstage xml schemas
* xacro.py -> xacro
* Contributors: Bence Magyar

1.12.1 (2018-02-13)
-------------------
* Merge pull request `#267 <https://github.com/pr2/pr2_common/issues/267>`_ from k-okada/maintainer
  change maintainer to ROS orphaned package maintainer
* change maintainer to ROS orphaned package maintainer
* Merge pull request `#266 <https://github.com/pr2/pr2_common/issues/266>`_ from furushchev/use-arg
  pr2.urdf.xacro: support xacro:arg
* pr2.urdf.xacro: support xacro:arg
* Merge pull request `#260 <https://github.com/pr2/pr2_common/issues/260>`_ from davetcoleman/inconsistent_namespace
  Fix inconsistent namespace redefinitions for xmlns:xacro
* Merge pull request `#259 <https://github.com/pr2/pr2_common/issues/259>`_ from davetcoleman/prepend_xacro_namespace
  Prepend xacro tags with xacro xml namespace
* Merge pull request `#258 <https://github.com/pr2/pr2_common/issues/258>`_ from PR2/indigo-devel
  Sync Indigo into Kinetic
* Prepend xacro tags with xacro xml namespace
* Fix inconsistent namespace redefinitions for xmlns:xacro
* Merge pull request `#255 <https://github.com/pr2/pr2_common/issues/255>`_ from furushchev/fix-gripper
  [pr2_description] fix: gripper reduction 3141.6 -> 314.16
* [pr2_description] fix: gripper reduction 3141.6 -> 314.16
* Contributors: Dave Coleman, Devon Ash, Furushchev, Kei Okada

1.11.9 (2015-02-10)
-------------------
* Updated maintainership
* Contributors: TheDash

1.11.8 (2015-01-13)
-------------------
* liburdfdom-dev dep
* Contributors: dash

1.11.7 (2015-01-12)
-------------------
* Fixed changelogs manually
* Merge conflicts
* Changelogs
* Changelogs
* Changelogs
* Changelogs
* Contributors: TheDash, dash

1.11.5 (2014-12-16)
-------------------
* when using ROS Indigo and Gazebo 2.2.3, the name specified here must be <link_name>_collision
* made test_urdf independent from ros package urdfdom by using liburdfdom-dev  directly as its recommended in the package description of urdfdom
* made test_urdf independent from ros package urdfdom by using liburdfdom-dev  directly as its recommended in the package description of urdfdom
* removed developers warning in pr2_descriptions CMakeLists.txt
* Contributors: Arne Hitzmann, Kei Okada
