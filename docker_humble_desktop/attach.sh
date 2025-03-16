export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export DISPLAY=unix$DISPLAY
export QT_X11_NO_MITSHM=1
export PYTHONPATH=/home/xplore/dev_ws/install/rover_pkg/lib/python3.10/site-packages:/home/xplore/dev_ws/install/custom_msg/local/lib/python3.10/dist-packages:/opt/ros/humble/install/local/lib/python3.10/dist-packages:/opt/ros/humble/install/lib/python3.10/site-packages:/opt/ros/humble/local/lib/python3.10/dist-packages:/opt/ros/humble/lib/python3.10/site-packages
source install/setup.bash


# The command execute 
# 1) export a python path for ros2 (errors from rosidl adapter)
# 2) export cyclone dds for ros2
# 3) source ros2
# 4) export some environement variables for X11 forwarding