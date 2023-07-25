#!/bin/sh
#exec >> launch_output.log 2>&1

echo "xplore" > pass.tmp
su root < pass.tmp
. ~/.bashrc
. /opt/ros/foxy/setup.sh

cd Desktop/ROVER/rover_ws
. install/setup.sh
ros2 run rover_pkg rover
