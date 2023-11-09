// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from xplore_interfaces:msg/CameraError.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "xplore_interfaces/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "xplore_interfaces/msg/detail/camera_error__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace xplore_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_xplore_interfaces
cdr_serialize(
  const xplore_interfaces::msg::CameraError & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_xplore_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  xplore_interfaces::msg::CameraError & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_xplore_interfaces
get_serialized_size(
  const xplore_interfaces::msg::CameraError & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_xplore_interfaces
max_serialized_size_CameraError(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace xplore_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_xplore_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, xplore_interfaces, msg, CameraError)();

#ifdef __cplusplus
}
#endif

#endif  // XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
