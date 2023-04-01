#!/bin/sh
cd CS_workspace/cs_ws
colcon build
source install/setup.bash
ros2 run rover_pkg rover