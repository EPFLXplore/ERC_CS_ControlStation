// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from xplore_interfaces:msg/CameraError.idl
// generated code does not contain a copyright notice
#include "xplore_interfaces/msg/detail/camera_error__rosidl_typesupport_fastrtps_cpp.hpp"
#include "xplore_interfaces/msg/detail/camera_error__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

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
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: index
  cdr << ros_message.index;
  // Member: ip_adresse
  cdr << ros_message.ip_adresse;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_xplore_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  xplore_interfaces::msg::CameraError & ros_message)
{
  // Member: index
  cdr >> ros_message.index;

  // Member: ip_adresse
  cdr >> ros_message.ip_adresse;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_xplore_interfaces
get_serialized_size(
  const xplore_interfaces::msg::CameraError & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: index
  {
    size_t item_size = sizeof(ros_message.index);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ip_adresse
  {
    size_t item_size = sizeof(ros_message.ip_adresse);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_xplore_interfaces
max_serialized_size_CameraError(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: index
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: ip_adresse
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static bool _CameraError__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const xplore_interfaces::msg::CameraError *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _CameraError__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<xplore_interfaces::msg::CameraError *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _CameraError__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const xplore_interfaces::msg::CameraError *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _CameraError__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_CameraError(full_bounded, 0);
}

static message_type_support_callbacks_t _CameraError__callbacks = {
  "xplore_interfaces::msg",
  "CameraError",
  _CameraError__cdr_serialize,
  _CameraError__cdr_deserialize,
  _CameraError__get_serialized_size,
  _CameraError__max_serialized_size
};

static rosidl_message_type_support_t _CameraError__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_CameraError__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace xplore_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_xplore_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<xplore_interfaces::msg::CameraError>()
{
  return &xplore_interfaces::msg::typesupport_fastrtps_cpp::_CameraError__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, xplore_interfaces, msg, CameraError)() {
  return &xplore_interfaces::msg::typesupport_fastrtps_cpp::_CameraError__handle;
}

#ifdef __cplusplus
}
#endif
