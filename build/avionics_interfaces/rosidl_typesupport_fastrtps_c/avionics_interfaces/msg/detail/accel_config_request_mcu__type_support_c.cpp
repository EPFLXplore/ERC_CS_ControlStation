// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from avionics_interfaces:msg/AccelConfigRequestMCU.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/accel_config_request_mcu__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "avionics_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "avionics_interfaces/msg/detail/accel_config_request_mcu__struct.h"
#include "avionics_interfaces/msg/detail/accel_config_request_mcu__functions.h"
#include "fastcdr/Cdr.h"

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

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _AccelConfigRequestMCU__ros_msg_type = avionics_interfaces__msg__AccelConfigRequestMCU;

static bool _AccelConfigRequestMCU__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _AccelConfigRequestMCU__ros_msg_type * ros_message = static_cast<const _AccelConfigRequestMCU__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr << ros_message->id;
  }

  // Field name: req_bias
  {
    cdr << (ros_message->req_bias ? true : false);
  }

  // Field name: req_transform
  {
    cdr << (ros_message->req_transform ? true : false);
  }

  return true;
}

static bool _AccelConfigRequestMCU__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _AccelConfigRequestMCU__ros_msg_type * ros_message = static_cast<_AccelConfigRequestMCU__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr >> ros_message->id;
  }

  // Field name: req_bias
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->req_bias = tmp ? true : false;
  }

  // Field name: req_transform
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->req_transform = tmp ? true : false;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t get_serialized_size_avionics_interfaces__msg__AccelConfigRequestMCU(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _AccelConfigRequestMCU__ros_msg_type * ros_message = static_cast<const _AccelConfigRequestMCU__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name id
  {
    size_t item_size = sizeof(ros_message->id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name req_bias
  {
    size_t item_size = sizeof(ros_message->req_bias);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name req_transform
  {
    size_t item_size = sizeof(ros_message->req_transform);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _AccelConfigRequestMCU__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_avionics_interfaces__msg__AccelConfigRequestMCU(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t max_serialized_size_avionics_interfaces__msg__AccelConfigRequestMCU(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: req_bias
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: req_transform
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _AccelConfigRequestMCU__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_avionics_interfaces__msg__AccelConfigRequestMCU(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_AccelConfigRequestMCU = {
  "avionics_interfaces::msg",
  "AccelConfigRequestMCU",
  _AccelConfigRequestMCU__cdr_serialize,
  _AccelConfigRequestMCU__cdr_deserialize,
  _AccelConfigRequestMCU__get_serialized_size,
  _AccelConfigRequestMCU__max_serialized_size
};

static rosidl_message_type_support_t _AccelConfigRequestMCU__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_AccelConfigRequestMCU,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, avionics_interfaces, msg, AccelConfigRequestMCU)() {
  return &_AccelConfigRequestMCU__type_support;
}

#if defined(__cplusplus)
}
#endif
