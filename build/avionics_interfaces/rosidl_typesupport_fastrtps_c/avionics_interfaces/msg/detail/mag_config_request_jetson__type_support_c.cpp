// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from avionics_interfaces:msg/MagConfigRequestJetson.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/mag_config_request_jetson__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "avionics_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "avionics_interfaces/msg/detail/mag_config_request_jetson__struct.h"
#include "avionics_interfaces/msg/detail/mag_config_request_jetson__functions.h"
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


using _MagConfigRequestJetson__ros_msg_type = avionics_interfaces__msg__MagConfigRequestJetson;

static bool _MagConfigRequestJetson__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _MagConfigRequestJetson__ros_msg_type * ros_message = static_cast<const _MagConfigRequestJetson__ros_msg_type *>(untyped_ros_message);
  // Field name: destination_id
  {
    cdr << ros_message->destination_id;
  }

  // Field name: hard_iron
  {
    size_t size = 3;
    auto array_ptr = ros_message->hard_iron;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: soft_iron
  {
    size_t size = 9;
    auto array_ptr = ros_message->soft_iron;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: remote_command
  {
    cdr << (ros_message->remote_command ? true : false);
  }

  // Field name: set_hard_iron
  {
    cdr << (ros_message->set_hard_iron ? true : false);
  }

  // Field name: set_soft_iron
  {
    cdr << (ros_message->set_soft_iron ? true : false);
  }

  return true;
}

static bool _MagConfigRequestJetson__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _MagConfigRequestJetson__ros_msg_type * ros_message = static_cast<_MagConfigRequestJetson__ros_msg_type *>(untyped_ros_message);
  // Field name: destination_id
  {
    cdr >> ros_message->destination_id;
  }

  // Field name: hard_iron
  {
    size_t size = 3;
    auto array_ptr = ros_message->hard_iron;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: soft_iron
  {
    size_t size = 9;
    auto array_ptr = ros_message->soft_iron;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: remote_command
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->remote_command = tmp ? true : false;
  }

  // Field name: set_hard_iron
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->set_hard_iron = tmp ? true : false;
  }

  // Field name: set_soft_iron
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->set_soft_iron = tmp ? true : false;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t get_serialized_size_avionics_interfaces__msg__MagConfigRequestJetson(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _MagConfigRequestJetson__ros_msg_type * ros_message = static_cast<const _MagConfigRequestJetson__ros_msg_type *>(untyped_ros_message);
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
  // field.name hard_iron
  {
    size_t array_size = 3;
    auto array_ptr = ros_message->hard_iron;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name soft_iron
  {
    size_t array_size = 9;
    auto array_ptr = ros_message->soft_iron;
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
  // field.name set_hard_iron
  {
    size_t item_size = sizeof(ros_message->set_hard_iron);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name set_soft_iron
  {
    size_t item_size = sizeof(ros_message->set_soft_iron);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _MagConfigRequestJetson__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_avionics_interfaces__msg__MagConfigRequestJetson(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t max_serialized_size_avionics_interfaces__msg__MagConfigRequestJetson(
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
  // member: hard_iron
  {
    size_t array_size = 3;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: soft_iron
  {
    size_t array_size = 9;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: remote_command
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: set_hard_iron
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: set_soft_iron
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _MagConfigRequestJetson__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_avionics_interfaces__msg__MagConfigRequestJetson(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_MagConfigRequestJetson = {
  "avionics_interfaces::msg",
  "MagConfigRequestJetson",
  _MagConfigRequestJetson__cdr_serialize,
  _MagConfigRequestJetson__cdr_deserialize,
  _MagConfigRequestJetson__get_serialized_size,
  _MagConfigRequestJetson__max_serialized_size
};

static rosidl_message_type_support_t _MagConfigRequestJetson__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_MagConfigRequestJetson,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, avionics_interfaces, msg, MagConfigRequestJetson)() {
  return &_MagConfigRequestJetson__type_support;
}

#if defined(__cplusplus)
}
#endif
