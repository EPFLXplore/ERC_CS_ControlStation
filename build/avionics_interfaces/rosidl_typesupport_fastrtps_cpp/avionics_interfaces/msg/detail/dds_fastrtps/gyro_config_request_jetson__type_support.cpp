// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from avionics_interfaces:msg/GyroConfigRequestJetson.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/gyro_config_request_jetson__rosidl_typesupport_fastrtps_cpp.hpp"
#include "avionics_interfaces/msg/detail/gyro_config_request_jetson__struct.hpp"

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

namespace avionics_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avionics_interfaces
cdr_serialize(
  const avionics_interfaces::msg::GyroConfigRequestJetson & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: destination_id
  cdr << ros_message.destination_id;
  // Member: bias
  {
    cdr << ros_message.bias;
  }
  // Member: remote_command
  cdr << (ros_message.remote_command ? true : false);
  // Member: set_bias
  cdr << (ros_message.set_bias ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avionics_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  avionics_interfaces::msg::GyroConfigRequestJetson & ros_message)
{
  // Member: destination_id
  cdr >> ros_message.destination_id;

  // Member: bias
  {
    cdr >> ros_message.bias;
  }

  // Member: remote_command
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.remote_command = tmp ? true : false;
  }

  // Member: set_bias
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.set_bias = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avionics_interfaces
get_serialized_size(
  const avionics_interfaces::msg::GyroConfigRequestJetson & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: destination_id
  {
    size_t item_size = sizeof(ros_message.destination_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: bias
  {
    size_t array_size = 3;
    size_t item_size = sizeof(ros_message.bias[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: remote_command
  {
    size_t item_size = sizeof(ros_message.remote_command);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: set_bias
  {
    size_t item_size = sizeof(ros_message.set_bias);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avionics_interfaces
max_serialized_size_GyroConfigRequestJetson(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: destination_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: bias
  {
    size_t array_size = 3;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: remote_command
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: set_bias
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _GyroConfigRequestJetson__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const avionics_interfaces::msg::GyroConfigRequestJetson *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _GyroConfigRequestJetson__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<avionics_interfaces::msg::GyroConfigRequestJetson *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _GyroConfigRequestJetson__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const avionics_interfaces::msg::GyroConfigRequestJetson *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _GyroConfigRequestJetson__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_GyroConfigRequestJetson(full_bounded, 0);
}

static message_type_support_callbacks_t _GyroConfigRequestJetson__callbacks = {
  "avionics_interfaces::msg",
  "GyroConfigRequestJetson",
  _GyroConfigRequestJetson__cdr_serialize,
  _GyroConfigRequestJetson__cdr_deserialize,
  _GyroConfigRequestJetson__get_serialized_size,
  _GyroConfigRequestJetson__max_serialized_size
};

static rosidl_message_type_support_t _GyroConfigRequestJetson__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_GyroConfigRequestJetson__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace avionics_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_avionics_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<avionics_interfaces::msg::GyroConfigRequestJetson>()
{
  return &avionics_interfaces::msg::typesupport_fastrtps_cpp::_GyroConfigRequestJetson__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, avionics_interfaces, msg, GyroConfigRequestJetson)() {
  return &avionics_interfaces::msg::typesupport_fastrtps_cpp::_GyroConfigRequestJetson__handle;
}

#ifdef __cplusplus
}
#endif
