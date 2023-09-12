// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from avionics_interfaces:msg/MassConfigRequestMCU.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/mass_config_request_mcu__rosidl_typesupport_fastrtps_cpp.hpp"
#include "avionics_interfaces/msg/detail/mass_config_request_mcu__struct.hpp"

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
  const avionics_interfaces::msg::MassConfigRequestMCU & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: id
  cdr << ros_message.id;
  // Member: req_offset
  cdr << (ros_message.req_offset ? true : false);
  // Member: req_scale
  cdr << (ros_message.req_scale ? true : false);
  // Member: req_alpha
  cdr << (ros_message.req_alpha ? true : false);
  // Member: req_channels_status
  cdr << (ros_message.req_channels_status ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avionics_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  avionics_interfaces::msg::MassConfigRequestMCU & ros_message)
{
  // Member: id
  cdr >> ros_message.id;

  // Member: req_offset
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.req_offset = tmp ? true : false;
  }

  // Member: req_scale
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.req_scale = tmp ? true : false;
  }

  // Member: req_alpha
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.req_alpha = tmp ? true : false;
  }

  // Member: req_channels_status
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.req_channels_status = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avionics_interfaces
get_serialized_size(
  const avionics_interfaces::msg::MassConfigRequestMCU & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: id
  {
    size_t item_size = sizeof(ros_message.id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: req_offset
  {
    size_t item_size = sizeof(ros_message.req_offset);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: req_scale
  {
    size_t item_size = sizeof(ros_message.req_scale);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: req_alpha
  {
    size_t item_size = sizeof(ros_message.req_alpha);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: req_channels_status
  {
    size_t item_size = sizeof(ros_message.req_channels_status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avionics_interfaces
max_serialized_size_MassConfigRequestMCU(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: req_offset
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: req_scale
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: req_alpha
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: req_channels_status
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _MassConfigRequestMCU__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const avionics_interfaces::msg::MassConfigRequestMCU *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _MassConfigRequestMCU__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<avionics_interfaces::msg::MassConfigRequestMCU *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _MassConfigRequestMCU__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const avionics_interfaces::msg::MassConfigRequestMCU *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _MassConfigRequestMCU__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_MassConfigRequestMCU(full_bounded, 0);
}

static message_type_support_callbacks_t _MassConfigRequestMCU__callbacks = {
  "avionics_interfaces::msg",
  "MassConfigRequestMCU",
  _MassConfigRequestMCU__cdr_serialize,
  _MassConfigRequestMCU__cdr_deserialize,
  _MassConfigRequestMCU__get_serialized_size,
  _MassConfigRequestMCU__max_serialized_size
};

static rosidl_message_type_support_t _MassConfigRequestMCU__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_MassConfigRequestMCU__callbacks,
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
get_message_type_support_handle<avionics_interfaces::msg::MassConfigRequestMCU>()
{
  return &avionics_interfaces::msg::typesupport_fastrtps_cpp::_MassConfigRequestMCU__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, avionics_interfaces, msg, MassConfigRequestMCU)() {
  return &avionics_interfaces::msg::typesupport_fastrtps_cpp::_MassConfigRequestMCU__handle;
}

#ifdef __cplusplus
}
#endif
