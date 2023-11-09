// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from avionics_interfaces:msg/ServoConfigRequestJetson.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/servo_config_request_jetson__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "avionics_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "avionics_interfaces/msg/detail/servo_config_request_jetson__struct.h"
#include "avionics_interfaces/msg/detail/servo_config_request_jetson__functions.h"
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


using _ServoConfigRequestJetson__ros_msg_type = avionics_interfaces__msg__ServoConfigRequestJetson;

static bool _ServoConfigRequestJetson__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ServoConfigRequestJetson__ros_msg_type * ros_message = static_cast<const _ServoConfigRequestJetson__ros_msg_type *>(untyped_ros_message);
  // Field name: destination_id
  {
    cdr << ros_message->destination_id;
  }

  // Field name: min_duty
  {
    size_t size = 4;
    auto array_ptr = ros_message->min_duty;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: max_duty
  {
    size_t size = 4;
    auto array_ptr = ros_message->max_duty;
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

  // Field name: remote_command
  {
    cdr << (ros_message->remote_command ? true : false);
  }

  // Field name: set_min_duty
  {
    cdr << (ros_message->set_min_duty ? true : false);
  }

  // Field name: set_max_duty
  {
    cdr << (ros_message->set_max_duty ? true : false);
  }

  // Field name: set_min_angles
  {
    cdr << (ros_message->set_min_angles ? true : false);
  }

  // Field name: set_max_angles
  {
    cdr << (ros_message->set_max_angles ? true : false);
  }

  return true;
}

static bool _ServoConfigRequestJetson__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ServoConfigRequestJetson__ros_msg_type * ros_message = static_cast<_ServoConfigRequestJetson__ros_msg_type *>(untyped_ros_message);
  // Field name: destination_id
  {
    cdr >> ros_message->destination_id;
  }

  // Field name: min_duty
  {
    size_t size = 4;
    auto array_ptr = ros_message->min_duty;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: max_duty
  {
    size_t size = 4;
    auto array_ptr = ros_message->max_duty;
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

  // Field name: remote_command
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->remote_command = tmp ? true : false;
  }

  // Field name: set_min_duty
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->set_min_duty = tmp ? true : false;
  }

  // Field name: set_max_duty
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->set_max_duty = tmp ? true : false;
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

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t get_serialized_size_avionics_interfaces__msg__ServoConfigRequestJetson(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ServoConfigRequestJetson__ros_msg_type * ros_message = static_cast<const _ServoConfigRequestJetson__ros_msg_type *>(untyped_ros_message);
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
  // field.name min_duty
  {
    size_t array_size = 4;
    auto array_ptr = ros_message->min_duty;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name max_duty
  {
    size_t array_size = 4;
    auto array_ptr = ros_message->max_duty;
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
  // field.name remote_command
  {
    size_t item_size = sizeof(ros_message->remote_command);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name set_min_duty
  {
    size_t item_size = sizeof(ros_message->set_min_duty);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name set_max_duty
  {
    size_t item_size = sizeof(ros_message->set_max_duty);
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

  return current_alignment - initial_alignment;
}

static uint32_t _ServoConfigRequestJetson__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_avionics_interfaces__msg__ServoConfigRequestJetson(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t max_serialized_size_avionics_interfaces__msg__ServoConfigRequestJetson(
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
  // member: min_duty
  {
    size_t array_size = 4;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: max_duty
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
  // member: remote_command
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: set_min_duty
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: set_max_duty
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

  return current_alignment - initial_alignment;
}

static size_t _ServoConfigRequestJetson__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_avionics_interfaces__msg__ServoConfigRequestJetson(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_ServoConfigRequestJetson = {
  "avionics_interfaces::msg",
  "ServoConfigRequestJetson",
  _ServoConfigRequestJetson__cdr_serialize,
  _ServoConfigRequestJetson__cdr_deserialize,
  _ServoConfigRequestJetson__get_serialized_size,
  _ServoConfigRequestJetson__max_serialized_size
};

static rosidl_message_type_support_t _ServoConfigRequestJetson__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ServoConfigRequestJetson,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, avionics_interfaces, msg, ServoConfigRequestJetson)() {
  return &_ServoConfigRequestJetson__type_support;
}

#if defined(__cplusplus)
}
#endif
