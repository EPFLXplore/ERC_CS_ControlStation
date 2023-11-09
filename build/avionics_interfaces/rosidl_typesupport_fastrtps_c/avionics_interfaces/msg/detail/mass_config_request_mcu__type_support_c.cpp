// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from avionics_interfaces:msg/MassConfigRequestMCU.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/mass_config_request_mcu__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "avionics_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "avionics_interfaces/msg/detail/mass_config_request_mcu__struct.h"
#include "avionics_interfaces/msg/detail/mass_config_request_mcu__functions.h"
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


using _MassConfigRequestMCU__ros_msg_type = avionics_interfaces__msg__MassConfigRequestMCU;

static bool _MassConfigRequestMCU__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _MassConfigRequestMCU__ros_msg_type * ros_message = static_cast<const _MassConfigRequestMCU__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr << ros_message->id;
  }

  // Field name: req_offset
  {
    cdr << (ros_message->req_offset ? true : false);
  }

  // Field name: req_scale
  {
    cdr << (ros_message->req_scale ? true : false);
  }

  // Field name: req_alpha
  {
    cdr << (ros_message->req_alpha ? true : false);
  }

  // Field name: req_channels_status
  {
    cdr << (ros_message->req_channels_status ? true : false);
  }

  return true;
}

static bool _MassConfigRequestMCU__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _MassConfigRequestMCU__ros_msg_type * ros_message = static_cast<_MassConfigRequestMCU__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr >> ros_message->id;
  }

  // Field name: req_offset
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->req_offset = tmp ? true : false;
  }

  // Field name: req_scale
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->req_scale = tmp ? true : false;
  }

  // Field name: req_alpha
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->req_alpha = tmp ? true : false;
  }

  // Field name: req_channels_status
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->req_channels_status = tmp ? true : false;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t get_serialized_size_avionics_interfaces__msg__MassConfigRequestMCU(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _MassConfigRequestMCU__ros_msg_type * ros_message = static_cast<const _MassConfigRequestMCU__ros_msg_type *>(untyped_ros_message);
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
  // field.name req_offset
  {
    size_t item_size = sizeof(ros_message->req_offset);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name req_scale
  {
    size_t item_size = sizeof(ros_message->req_scale);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name req_alpha
  {
    size_t item_size = sizeof(ros_message->req_alpha);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name req_channels_status
  {
    size_t item_size = sizeof(ros_message->req_channels_status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _MassConfigRequestMCU__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_avionics_interfaces__msg__MassConfigRequestMCU(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t max_serialized_size_avionics_interfaces__msg__MassConfigRequestMCU(
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
  // member: req_offset
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: req_scale
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: req_alpha
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: req_channels_status
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _MassConfigRequestMCU__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_avionics_interfaces__msg__MassConfigRequestMCU(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_MassConfigRequestMCU = {
  "avionics_interfaces::msg",
  "MassConfigRequestMCU",
  _MassConfigRequestMCU__cdr_serialize,
  _MassConfigRequestMCU__cdr_deserialize,
  _MassConfigRequestMCU__get_serialized_size,
  _MassConfigRequestMCU__max_serialized_size
};

static rosidl_message_type_support_t _MassConfigRequestMCU__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_MassConfigRequestMCU,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, avionics_interfaces, msg, MassConfigRequestMCU)() {
  return &_MassConfigRequestMCU__type_support;
}

#if defined(__cplusplus)
}
#endif
