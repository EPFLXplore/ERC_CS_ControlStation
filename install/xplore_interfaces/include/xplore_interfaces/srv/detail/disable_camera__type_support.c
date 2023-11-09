// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from xplore_interfaces:srv/DisableCamera.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "xplore_interfaces/srv/detail/disable_camera__rosidl_typesupport_introspection_c.h"
#include "xplore_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "xplore_interfaces/srv/detail/disable_camera__functions.h"
#include "xplore_interfaces/srv/detail/disable_camera__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  xplore_interfaces__srv__DisableCamera_Request__init(message_memory);
}

void DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_fini_function(void * message_memory)
{
  xplore_interfaces__srv__DisableCamera_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_message_member_array[1] = {
  {
    "index",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(xplore_interfaces__srv__DisableCamera_Request, index),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_message_members = {
  "xplore_interfaces__srv",  // message namespace
  "DisableCamera_Request",  // message name
  1,  // number of fields
  sizeof(xplore_interfaces__srv__DisableCamera_Request),
  DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_message_member_array,  // message members
  DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_message_type_support_handle = {
  0,
  &DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_xplore_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, xplore_interfaces, srv, DisableCamera_Request)() {
  if (!DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_message_type_support_handle.typesupport_identifier) {
    DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &DisableCamera_Request__rosidl_typesupport_introspection_c__DisableCamera_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "xplore_interfaces/srv/detail/disable_camera__rosidl_typesupport_introspection_c.h"
// already included above
// #include "xplore_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "xplore_interfaces/srv/detail/disable_camera__functions.h"
// already included above
// #include "xplore_interfaces/srv/detail/disable_camera__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  xplore_interfaces__srv__DisableCamera_Response__init(message_memory);
}

void DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_fini_function(void * message_memory)
{
  xplore_interfaces__srv__DisableCamera_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_message_member_array[1] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(xplore_interfaces__srv__DisableCamera_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_message_members = {
  "xplore_interfaces__srv",  // message namespace
  "DisableCamera_Response",  // message name
  1,  // number of fields
  sizeof(xplore_interfaces__srv__DisableCamera_Response),
  DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_message_member_array,  // message members
  DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_message_type_support_handle = {
  0,
  &DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_xplore_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, xplore_interfaces, srv, DisableCamera_Response)() {
  if (!DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_message_type_support_handle.typesupport_identifier) {
    DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &DisableCamera_Response__rosidl_typesupport_introspection_c__DisableCamera_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "xplore_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "xplore_interfaces/srv/detail/disable_camera__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers xplore_interfaces__srv__detail__disable_camera__rosidl_typesupport_introspection_c__DisableCamera_service_members = {
  "xplore_interfaces__srv",  // service namespace
  "DisableCamera",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // xplore_interfaces__srv__detail__disable_camera__rosidl_typesupport_introspection_c__DisableCamera_Request_message_type_support_handle,
  NULL  // response message
  // xplore_interfaces__srv__detail__disable_camera__rosidl_typesupport_introspection_c__DisableCamera_Response_message_type_support_handle
};

static rosidl_service_type_support_t xplore_interfaces__srv__detail__disable_camera__rosidl_typesupport_introspection_c__DisableCamera_service_type_support_handle = {
  0,
  &xplore_interfaces__srv__detail__disable_camera__rosidl_typesupport_introspection_c__DisableCamera_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, xplore_interfaces, srv, DisableCamera_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, xplore_interfaces, srv, DisableCamera_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_xplore_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, xplore_interfaces, srv, DisableCamera)() {
  if (!xplore_interfaces__srv__detail__disable_camera__rosidl_typesupport_introspection_c__DisableCamera_service_type_support_handle.typesupport_identifier) {
    xplore_interfaces__srv__detail__disable_camera__rosidl_typesupport_introspection_c__DisableCamera_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)xplore_interfaces__srv__detail__disable_camera__rosidl_typesupport_introspection_c__DisableCamera_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, xplore_interfaces, srv, DisableCamera_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, xplore_interfaces, srv, DisableCamera_Response)()->data;
  }

  return &xplore_interfaces__srv__detail__disable_camera__rosidl_typesupport_introspection_c__DisableCamera_service_type_support_handle;
}
