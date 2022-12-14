set(CMAKE_CXX_STANDARD 14)
project(control_station)

find_package(rosidl_default_generators REQUIRED)

# For each dependent message package, add find_package(message_package REQUIRED) 
# and replace the CMake function call to generate_messages with rosidl_generate_interfaces.
# This will replace add_message_files and add_service_files listing of all the message and service files, 
# which can be removed.

find_package(ament_cmake REQUIRED)
find_package(actionlib_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(rospy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)