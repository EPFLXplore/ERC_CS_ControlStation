// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from avionics_interfaces:msg/MassCalibOffset.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/mass_calib_offset__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "avionics_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "avionics_interfaces/msg/detail/mass_calib_offset__struct.h"
#include "avionics_interfaces/msg/detail/mass_calib_offset__functions.h"
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


using _MassCalibOffset__ros_msg_type = avionics_interfaces__msg__MassCalibOffset;

static bool _MassCalibOffset__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _MassCalibOffset__ros_msg_type * ros_message = static_cast<const _MassCalibOffset__ros_msg_type *>(untyped_ros_message);
  // Field name: destination_id
  {
    cdr << ros_message->destination_id;
  }

  // Field name: channel
  {
    cdr << ros_message->channel;
  }

  return true;
}

static bool _MassCalibOffset__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _MassCalibOffset__ros_msg_type * ros_message = static_cast<_MassCalibOffset__ros_msg_type *>(untyped_ros_message);
  // Field name: destination_id
  {
    cdr >> ros_message->destination_id;
  }

  // Field name: channel
  {
    cdr >> ros_message->channel;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t get_serialized_size_avionics_interfaces__msg__MassCalibOffset(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _MassCalibOffset__ros_msg_type * ros_message = static_cast<const _MassCalibOffset__ros_msg_type *>(untyped_ros_message);
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

  return current_alignment - initial_alignment;
}

static uint32_t _MassCalibOffset__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_avionics_interfaces__msg__MassCalibOffset(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t max_serialized_size_avionics_interfaces__msg__MassCalibOffset(
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

  return current_alignment - initial_alignment;
}

static size_t _MassCalibOffset__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_avionics_interfaces__msg__MassCalibOffset(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_MassCalibOffset = {
  "avionics_interfaces::msg",
  "MassCalibOffset",
  _MassCalibOffset__cdr_serialize,
  _MassCalibOffset__cdr_deserialize,
  _MassCalibOffset__get_serialized_size,
  _MassCalibOffset__max_serialized_size
};

static rosidl_message_type_support_t _MassCalibOffset__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_MassCalibOffset,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, avionics_interfaces, msg, MassCalibOffset)() {
  return &_MassCalibOffset__type_support;
}

#if defined(__cplusplus)
}
#endif
