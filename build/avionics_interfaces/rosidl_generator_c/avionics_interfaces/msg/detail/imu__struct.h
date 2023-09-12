// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avionics_interfaces:msg/Imu.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__IMU__STRUCT_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__IMU__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'imu'
#include "sensor_msgs/msg/detail/imu__struct.h"

// Struct defined in msg/Imu in the package avionics_interfaces.
typedef struct avionics_interfaces__msg__Imu
{
  uint16_t id;
  sensor_msgs__msg__Imu imu;
} avionics_interfaces__msg__Imu;

// Struct for a sequence of avionics_interfaces__msg__Imu.
typedef struct avionics_interfaces__msg__Imu__Sequence
{
  avionics_interfaces__msg__Imu * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avionics_interfaces__msg__Imu__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__IMU__STRUCT_H_
