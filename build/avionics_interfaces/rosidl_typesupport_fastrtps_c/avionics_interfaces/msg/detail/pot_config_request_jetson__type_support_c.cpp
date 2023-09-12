// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from avionics_interfaces:msg/PotConfigRequestJetson.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/pot_config_request_jetson__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "avionics_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "avionics_interfaces/msg/detail/pot_config_request_jetson__struct.h"
#include "avionics_interfaces/msg/detail/pot_config_request_jetson__functions.h"
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


using _PotConfigRequestJetson__ros_msg_type = avionics_interfaces__msg__PotConfigRequestJetson;

static bool _PotConfigRequestJetson__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _PotConfigRequestJetson__ros_msg_type * ros_message = static_cast<const _PotConfigRequestJetson__ros_msg_type *>(untyped_ros_message);
  // Field name: destination_id
  {
    cdr << ros_message->destination_id;
  }

  // Field name: min_voltages
  {
    size_t size = 4;
    auto array_ptr = ros_message->min_voltages;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: max_voltages
  {
    size_t size = 4;
    auto array_ptr = ros_message->max_voltages;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: min_angles
  {
    size_t size = 4;
    auto array_ptr = ros_message->min_angles;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: max_angles
  {
    size_t size = 4;
    auto array_ptr = ros_message->max_angles;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: enabled_channels
  {
    size_t size = 4;
    auto array_ptr = ros_message->enabled_channels;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: remote_command
  {
    cdr << (ros_message->remote_command ? true : false);
  }

  // Field name: set_min_voltages
  {
    cdr << (ros_message->set_min_voltages ? true : false);
  }

  // Field name: set_max_voltages
  {
    cdr << (ros_message->set_max_voltages ? true : false);
  }

  // Field name: set_min_angles
  {
    cdr << (ros_message->set_min_angles ? true : false);
  }

  // Field name: set_max_angles
  {
    cdr << (ros_message->set_max_angles ? true : false);
  }

  // Field name: set_channels_status
  {
    cdr << (ros_message->set_channels_status ? true : false);
  }

  return true;
}

static bool _PotConfigRequestJetson__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _PotConfigRequestJetson__ros_msg_type * ros_message = static_cast<_PotConfigRequestJetson__ros_msg_type *>(untyped_ros_message);
  // Field name: destination_id
  {
    cdr >> ros_message->destination_id;
  }

  // Field name: min_voltages
  {
    size_t size = 4;
    auto array_ptr = ros_message->min_voltages;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: max_voltages
  {
    size_t size = 4;
    auto array_ptr = ros_message->max_voltages;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: min_angles
  {
    size_t size = 4;
    auto array_ptr = ros_message->min_angles;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: max_angles
  {
    size_t size = 4;
    auto array_ptr = ros_message->max_angles;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: enabled_channels
  {
    size_t size = 4;
    auto array_ptr = ros_message->enabled_channels;
    for (size_t i = 0; i < size; ++i) {
      uint8_t tmp;
      cdr >> tmp;
      array_ptr[i] = tmp ? true : false;
    }
  }

  // Field name: remote_command
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->remote_command = tmp ? true : false;
  }

  // Field name: set_min_voltages
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->set_min_voltages = tmp ? true : false;
  }

  // Field name: set_max_voltages
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->set_max_voltages = tmp ? true : false;
  }

  // Field name: set_min_angles
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->set_min_angles = tmp ? true : false;
  }

  // Field name: set_max_angles
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->set_max_angles = tmp ? true : false;
  }

  // Field name: set_channels_status
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->set_channels_status = tmp ? true : false;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t get_serialized_size_avionics_interfaces__msg__PotConfigRequestJetson(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _PotConfigRequestJetson__ros_msg_type * ros_message = static_cast<const _PotConfigRequestJetson__ros_msg_type *>(untyped_ros_message);
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
  // field.name min_voltages
  {
    size_t array_size = 4;
    auto array_ptr = ros_message->min_voltages;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name max_voltages
  {
    size_t array_size = 4;
    auto array_ptr = ros_message->max_voltages;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name min_angles
  {
    size_t array_size = 4;
    auto array_ptr = ros_message->min_angles;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name max_angles
  {
    size_t array_size = 4;
    auto array_ptr = ros_message->max_angles;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name enabled_channels
  {
    size_t array_size = 4;
    auto array_ptr = ros_message->enabled_channels;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name remote_command
  {
    size_t item_size = sizeof(ros_message->remote_command);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name set_min_voltages
  {
    size_t item_size = sizeof(ros_message->set_min_voltages);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name set_max_voltages
  {
    size_t item_size = sizeof(ros_message->set_max_voltages);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name set_min_angles
  {
    size_t item_size = sizeof(ros_message->set_min_angles);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name set_max_angles
  {
    size_t item_size = sizeof(ros_message->set_max_angles);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name set_channels_status
  {
    size_t item_size = sizeof(ros_message->set_channels_status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _PotConfigRequestJetson__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_avionics_interfaces__msg__PotConfigRequestJetson(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t max_serialized_size_avionics_interfaces__msg__PotConfigRequestJetson(
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
  // member: min_voltages
  {
    size_t array_size = 4;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: max_voltages
  {
    size_t array_size = 4;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: min_angles
  {
    size_t array_size = 4;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: max_angles
  {
    size_t array_size = 4;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: enabled_channels
  {
    size_t array_size = 4;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: remote_command
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: set_min_voltages
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: set_max_voltages
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: set_min_angles
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: set_max_angles
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: set_channels_status
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _PotConfigRequestJetson__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_avionics_interfaces__msg__PotConfigRequestJetson(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_PotConfigRequestJetson = {
  "avionics_interfaces::msg",
  "PotConfigRequestJetson",
  _PotConfigRequestJetson__cdr_serialize,
  _PotConfigRequestJetson__cdr_deserialize,
  _PotConfigRequestJetson__get_serialized_size,
  _PotConfigRequestJetson__max_serialized_size
};

static rosidl_message_type_support_t _PotConfigRequestJetson__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_PotConfigRequestJetson,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, avionics_interfaces, msg, PotConfigRequestJetson)() {
  return &_PotConfigRequestJetson__type_support;
}

#if defined(__cplusplus)
}
#endif
