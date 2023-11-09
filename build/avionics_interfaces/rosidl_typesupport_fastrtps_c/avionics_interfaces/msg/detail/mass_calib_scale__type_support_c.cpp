// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from avionics_interfaces:msg/MassCalibScale.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/mass_calib_scale__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "avionics_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "avionics_interfaces/msg/detail/mass_calib_scale__struct.h"
#include "avionics_interfaces/msg/detail/mass_calib_scale__functions.h"
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


using _MassCalibScale__ros_msg_type = avionics_interfaces__msg__MassCalibScale;

static bool _MassCalibScale__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _MassCalibScale__ros_msg_type * ros_message = static_cast<const _MassCalibScale__ros_msg_type *>(untyped_ros_message);
  // Field name: destination_id
  {
    cdr << ros_message->destination_id;
  }

  // Field name: channel
  {
    cdr << ros_message->channel;
  }

  // Field name: expected_weight
  {
    cdr << ros_message->expected_weight;
  }

  return true;
}

static bool _MassCalibScale__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _MassCalibScale__ros_msg_type * ros_message = static_cast<_MassCalibScale__ros_msg_type *>(untyped_ros_message);
  // Field name: destination_id
  {
    cdr >> ros_message->destination_id;
  }

  // Field name: channel
  {
    cdr >> ros_message->channel;
  }

  // Field name: expected_weight
  {
    cdr >> ros_message->expected_weight;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t get_serialized_size_avionics_interfaces__msg__MassCalibScale(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _MassCalibScale__ros_msg_type * ros_message = static_cast<const _MassCalibScale__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name destination_id
  {
    size_t item_size = sizeof(ros_message->destination_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name channel
  {
    size_t item_size = sizeof(ros_message->channel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name expected_weight
  {
    size_t item_size = sizeof(ros_message->expected_weight);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _MassCalibScale__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_avionics_interfaces__msg__MassCalibScale(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t max_serialized_size_avionics_interfaces__msg__MassCalibScale(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: destination_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: channel
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: expected_weight
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _MassCalibScale__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_avionics_interfaces__msg__MassCalibScale(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_MassCalibScale = {
  "avionics_interfaces::msg",
  "MassCalibScale",
  _MassCalibScale__cdr_serialize,
  _MassCalibScale__cdr_deserialize,
  _MassCalibScale__get_serialized_size,
  _MassCalibScale__max_serialized_size
};

static rosidl_message_type_support_t _MassCalibScale__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_MassCalibScale,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, avionics_interfaces, msg, MassCalibScale)() {
  return &_MassCalibScale__type_support;
}

#if defined(__cplusplus)
}
#endif
