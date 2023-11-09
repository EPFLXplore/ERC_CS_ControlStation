// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/ServoRequest.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SERVO_REQUEST__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__SERVO_REQUEST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/ServoRequest in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__ServoRequest
{
  uint16_t destination_id;
  uint8_t channel;
  float angle;
} avionics_interfaces__msg__ServoRequest;

// Struct for a sequence of avionics_interfaces__msg__ServoRequest.
typedef struct avionics_interfaces__msg__ServoRequest__Sequence
{
  avionics_interfaces__msg__ServoRequest * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__ServoRequest__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SERVO_REQUEST__STRUCT_H_
