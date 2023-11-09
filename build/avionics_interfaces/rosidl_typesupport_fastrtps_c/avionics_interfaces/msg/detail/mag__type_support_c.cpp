// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from avionics_interfaces:msg/Mag.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/mag__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "avionics_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "avionics_interfaces/msg/detail/mag__struct.h"
#include "avionics_interfaces/msg/detail/mag__functions.h"
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

#include "sensor_msgs/msg/detail/magnetic_field__functions.h"  // mag_cal, mag_raw

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_avionics_interfaces
size_t get_serialized_size_sensor_msgs__msg__MagneticField(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_avionics_interfaces
size_t max_serialized_size_sensor_msgs__msg__MagneticField(
  bool & full_bounded,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_avionics_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sensor_msgs, msg, MagneticField)();


using _Mag__ros_msg_type = avionics_interfaces__msg__Mag;

static bool _Mag__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Mag__ros_msg_type * ros_message = static_cast<const _Mag__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr << ros_message->id;
  }

  // Field name: mag_raw
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sensor_msgs, msg, MagneticField
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->mag_raw, cdr))
    {
      return false;
    }
  }

  // Field name: mag_cal
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sensor_msgs, msg, MagneticField
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->mag_cal, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _Mag__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Mag__ros_msg_type * ros_message = static_cast<_Mag__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr >> ros_message->id;
  }

  // Field name: mag_raw
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sensor_msgs, msg, MagneticField
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->mag_raw))
    {
      return false;
    }
  }

  // Field name: mag_cal
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sensor_msgs, msg, MagneticField
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->mag_cal))
    {
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t get_serialized_size_avionics_interfaces__msg__Mag(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Mag__ros_msg_type * ros_message = static_cast<const _Mag__ros_msg_type *>(untyped_ros_message);
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
  // field.name mag_raw

  current_alignment += get_serialized_size_sensor_msgs__msg__MagneticField(
    &(ros_message->mag_raw), current_alignment);
  // field.name mag_cal

  current_alignment += get_serialized_size_sensor_msgs__msg__MagneticField(
    &(ros_message->mag_cal), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _Mag__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_avionics_interfaces__msg__Mag(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avionics_interfaces
size_t max_serialized_size_avionics_interfaces__msg__Mag(
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
  // member: mag_raw
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_sensor_msgs__msg__MagneticField(
        full_bounded, current_alignment);
    }
  }
  // member: mag_cal
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_sensor_msgs__msg__MagneticField(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _Mag__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_avionics_interfaces__msg__Mag(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_Mag = {
  "avionics_interfaces::msg",
  "Mag",
  _Mag__cdr_serialize,
  _Mag__cdr_deserialize,
  _Mag__get_serialized_size,
  _Mag__max_serialized_size
};

static rosidl_message_type_support_t _Mag__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Mag,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, avionics_interfaces, msg, Mag)() {
  return &_Mag__type_support;
}

#if defined(__cplusplus)
}
#endif
