// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/NodeStateArray.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'node_state'
#include "rosidl_runtime_c/primitives_sequence.h"

// Struct defined in msg/NodeStateArray in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__NodeStateArray
{
  rosidl_runtime_c__boolean__Sequence node_state;
} avionics_interfaces__msg__NodeStateArray;

// Struct for a sequence of avionics_interfaces__msg__NodeStateArray.
typedef struct avionics_interfaces__msg__NodeStateArray__Sequence
{
  avionics_interfaces__msg__NodeStateArray * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__NodeStateArray__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__STRUCT_H_
