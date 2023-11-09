// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from avionics_interfaces:msg/ImuCalib.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/imu_calib__rosidl_typesupport_fastrtps_cpp.hpp"
#include "avionics_interfaces/msg/detail/imu_calib__struct.hpp"

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
  const avionics_interfaces::msg::ImuCalib & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: destination_id
  cdr << ros_message.destination_id;
  // Member: calib_offset_accel
  cdr << (ros_message.calib_offset_accel ? true : false);
  // Member: calib_offset_gyro
  cdr << (ros_message.calib_offset_gyro ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avionics_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  avionics_interfaces::msg::ImuCalib & ros_message)
{
  // Member: destination_id
  cdr >> ros_message.destination_id;

  // Member: calib_offset_accel
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.calib_offset_accel = tmp ? true : false;
  }

  // Member: calib_offset_gyro
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.calib_offset_gyro = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avionics_interfaces
get_serialized_size(
  const avionics_interfaces::msg::ImuCalib & ros_message,
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
  // Member: calib_offset_accel
  {
    size_t item_size = sizeof(ros_message.calib_offset_accel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: calib_offset_gyro
  {
    size_t item_size = sizeof(ros_message.calib_offset_gyro);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avionics_interfaces
max_serialized_size_ImuCalib(
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

  // Member: calib_offset_accel
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: calib_offset_gyro
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _ImuCalib__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const avionics_interfaces::msg::ImuCalib *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _ImuCalib__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<avionics_interfaces::msg::ImuCalib *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _ImuCalib__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const avionics_interfaces::msg::ImuCalib *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _ImuCalib__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ImuCalib(full_bounded, 0);
}

static message_type_support_callbacks_t _ImuCalib__callbacks = {
  "avionics_interfaces::msg",
  "ImuCalib",
  _ImuCalib__cdr_serialize,
  _ImuCalib__cdr_deserialize,
  _ImuCalib__get_serialized_size,
  _ImuCalib__max_serialized_size
};

static rosidl_message_type_support_t _ImuCalib__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_ImuCalib__callbacks,
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
get_message_type_support_handle<avionics_interfaces::msg::ImuCalib>()
{
  return &avionics_interfaces::msg::typesupport_fastrtps_cpp::_ImuCalib__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, avionics_interfaces, msg, ImuCalib)() {
  return &avionics_interfaces::msg::typesupport_fastrtps_cpp::_ImuCalib__handle;
}

#ifdef __cplusplus
}
#endif
