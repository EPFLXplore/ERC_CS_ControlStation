#!/bin/sh
exec >> launch_output.log 2>&1

. ~/.bashrc
. /opt/ros/foxy/setup.sh

cd CS_workspace/cs_ws
. install/setup.sh
ros2 run rover_pkg rover
