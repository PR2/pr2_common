#!/bin/bash

PR2_DEFS=`rospack find pr2_defs`
PR2_OGRE=`rospack find pr2_ogre`

mkdir -p $PR2_OGRE/Media/models/convex

rosrun ogre_tools stl_to_mesh $PR2_DEFS/meshes/*.stl $PR2_OGRE/Media/models
rosrun ogre_tools stl_to_mesh $PR2_DEFS/meshes/convex/*.stlb $PR2_OGRE/Media/models/convex
