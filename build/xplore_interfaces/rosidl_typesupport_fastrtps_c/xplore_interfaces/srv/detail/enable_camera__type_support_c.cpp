// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from xplore_interfaces:srv/EnableCamera.idl
// generated code does not contain a copyright notice
#include "xplore_interfaces/srv/detail/enable_camera__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "xplore_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "xplore_interfaces/srv/detail/enable_camera__struct.h"
#include "xplore_interfaces/srv/detail/enable_camera__functions.h"
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


using _EnableCamera_Request__ros_msg_type = xplore_interfaces__srv__EnableCamera_Request;

static bool _EnableCamera_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _EnableCamera_Request__ros_msg_type * ros_message = static_cast<const _EnableCamera_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: index
  {
    cdr << ros_message->index;
  }

  return true;
}

static bool _EnableCamera_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _EnableCamera_Request__ros_msg_type * ros_message = static_cast<_EnableCamera_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: index
  {
    cdr >> ros_message->index;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_xplore_interfaces
size_t get_serialized_size_xplore_interfaces__srv__EnableCamera_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _EnableCamera_Request__ros_msg_type * ros_message = static_cast<const _EnableCamera_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name index
  {
    size_t item_size = sizeof(ros_message->index);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _EnableCamera_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_xplore_interfaces__srv__EnableCamera_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_xplore_interfaces
size_t max_serialized_size_xplore_interfaces__srv__EnableCamera_Request(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: index
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _EnableCamera_Request__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_xplore_interfaces__srv__EnableCamera_Request(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_EnableCamera_Request = {
  "xplore_interfaces::srv",
  "EnableCamera_Request",
  _EnableCamera_Request__cdr_serialize,
  _EnableCamera_Request__cdr_deserialize,
  _EnableCamera_Request__get_serialized_size,
  _EnableCamera_Request__max_serialized_size
};

static rosidl_message_type_support_t _EnableCamera_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_EnableCamera_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, xplore_interfaces, srv, EnableCamera_Request)() {
  return &_EnableCamera_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "xplore_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "xplore_interfaces/srv/detail/enable_camera__struct.h"
// already included above
// #include "xplore_interfaces/srv/detail/enable_camera__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

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


using _EnableCamera_Response__ros_msg_type = xplore_interfaces__srv__EnableCamera_Response;

static bool _EnableCamera_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _EnableCamera_Response__ros_msg_type * ros_message = static_cast<const _EnableCamera_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    cdr << (ros_message->success ? true : false);
  }

  // Field name: ip_adresse
  {
    cdr << ros_message->ip_adresse;
  }

  return true;
}

static bool _EnableCamera_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _EnableCamera_Response__ros_msg_type * ros_message = static_cast<_EnableCamera_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->success = tmp ? true : false;
  }

  // Field name: ip_adresse
  {
    cdr >> ros_message->ip_adresse;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_xplore_interfaces
size_t get_serialized_size_xplore_interfaces__srv__EnableCamera_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _EnableCamera_Response__ros_msg_type * ros_message = static_cast<const _EnableCamera_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name success
  {
    size_t item_size = sizeof(ros_message->success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ip_adresse
  {
    size_t item_size = sizeof(ros_message->ip_adresse);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _EnableCamera_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_xplore_interfaces__srv__EnableCamera_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_xplore_interfaces
size_t max_serialized_size_xplore_interfaces__srv__EnableCamera_Response(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: success
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: ip_adresse
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _EnableCamera_Response__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_xplore_interfaces__srv__EnableCamera_Response(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_EnableCamera_Response = {
  "xplore_interfaces::srv",
  "EnableCamera_Response",
  _EnableCamera_Response__cdr_serialize,
  _EnableCamera_Response__cdr_deserialize,
  _EnableCamera_Response__get_serialized_size,
  _EnableCamera_Response__max_serialized_size
};

static rosidl_message_type_support_t _EnableCamera_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_EnableCamera_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, xplore_interfaces, srv, EnableCamera_Response)() {
  return &_EnableCamera_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "xplore_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "xplore_interfaces/srv/enable_camera.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t EnableCamera__callbacks = {
  "xplore_interfaces::srv",
  "EnableCamera",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, xplore_interfaces, srv, EnableCamera_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, xplore_interfaces, srv, EnableCamera_Response)(),
};

static rosidl_service_type_support_t EnableCamera__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &EnableCamera__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, xplore_interfaces, srv, EnableCamera)() {
  return &EnableCamera__handle;
}

#if defined(__cplusplus)
}
#endif
