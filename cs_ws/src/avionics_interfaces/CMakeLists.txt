cmake_minimum_required(VERSION 3.5)
project(avionics_interfaces)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

find_package(rosidl_default_generators REQUIRED)

find_package(sensor_msgs REQUIRED)

set(message_files
  "msg/AngleArray.msg"
  "msg/FourInOne.msg"
  "msg/Imu.msg"
  "msg/LaserResponse.msg"
  "msg/LEDResponse.msg"
  "msg/Mag.msg"
  "msg/MassArray.msg"
  "msg/NPK.msg"
  "msg/ServoResponse.msg"
  "msg/SpectroResponse.msg"
  "msg/Voltage.msg"

  "msg/NodeStateArray.msg"
)

set(message_request_files
  "msg/LaserRequest.msg"
  "msg/LEDRequest.msg"
  "msg/ServoRequest.msg"
  "msg/SpectroRequest.msg"
)

set(message_config_files
  "msg/MassConfigRequestJetson.msg"
  "msg/MassConfigRequestMCU.msg"
  "msg/MassConfigResponse.msg"

  "msg/PotConfigRequestJetson.msg"
  "msg/PotConfigRequestMCU.msg"
  "msg/PotConfigResponse.msg"

  "msg/ServoConfigRequestJetson.msg"
  "msg/ServoConfigRequestMCU.msg"
  "msg/ServoConfigResponse.msg"

  "msg/AccelConfigRequestJetson.msg"
  "msg/AccelConfigRequestMCU.msg"
  "msg/AccelConfigResponse.msg"

  "msg/GyroConfigRequestJetson.msg"
  "msg/GyroConfigRequestMCU.msg"
  "msg/GyroConfigResponse.msg"

  "msg/MagConfigRequestJetson.msg"
  "msg/MagConfigRequestMCU.msg"
  "msg/MagConfigResponse.msg"
)

set(message_calib_files
  "msg/MassCalibOffset.msg"
  "msg/MassCalibScale.msg"

  "msg/ImuCalib.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${message_files}
  ${message_request_files}
  ${message_config_files}
  ${message_calib_files}
  DEPENDENCIES sensor_msgs std_msgs
 )
ament_export_dependencies(rosidl_default_runtime)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
