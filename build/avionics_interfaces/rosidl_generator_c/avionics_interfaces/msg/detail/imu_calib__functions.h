// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from avionics_interfaces:msg/ImuCalib.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__IMU_CALIB__FUNCTIONS_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__IMU_CALIB__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "avionics_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "avionics_interfaces/msg/detail/imu_calib__struct.h"

/// Initialize msg/ImuCalib message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * avionics_interfaces__msg__ImuCalib
 * )) before or use
 * avionics_interfaces__msg__ImuCalib__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__ImuCalib__init(avionics_interfaces__msg__ImuCalib * msg);

/// Finalize msg/ImuCalib message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__ImuCalib__fini(avionics_interfaces__msg__ImuCalib * msg);

/// Create msg/ImuCalib message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * avionics_interfaces__msg__ImuCalib__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
avionics_interfaces__msg__ImuCalib *
avionics_interfaces__msg__ImuCalib__create();

/// Destroy msg/ImuCalib message.
/**
 * It calls
 * avionics_interfaces__msg__ImuCalib__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__ImuCalib__destroy(avionics_interfaces__msg__ImuCalib * msg);

/// Check for msg/ImuCalib message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__ImuCalib__are_equal(const avionics_interfaces__msg__ImuCalib * lhs, const avionics_interfaces__msg__ImuCalib * rhs);

/// Copy a msg/ImuCalib message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__ImuCalib__copy(
  const avionics_interfaces__msg__ImuCalib * input,
  avionics_interfaces__msg__ImuCalib * output);

/// Initialize array of msg/ImuCalib messages.
/**
 * It allocates the memory for the number of elements and calls
 * avionics_interfaces__msg__ImuCalib__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__ImuCalib__Sequence__init(avionics_interfaces__msg__ImuCalib__Sequence * array, size_t size);

/// Finalize array of msg/ImuCalib messages.
/**
 * It calls
 * avionics_interfaces__msg__ImuCalib__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__ImuCalib__Sequence__fini(avionics_interfaces__msg__ImuCalib__Sequence * array);

/// Create array of msg/ImuCalib messages.
/**
 * It allocates the memory for the array and calls
 * avionics_interfaces__msg__ImuCalib__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
avionics_interfaces__msg__ImuCalib__Sequence *
avionics_interfaces__msg__ImuCalib__Sequence__create(size_t size);

/// Destroy array of msg/ImuCalib messages.
/**
 * It calls
 * avionics_interfaces__msg__ImuCalib__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__ImuCalib__Sequence__destroy(avionics_interfaces__msg__ImuCalib__Sequence * array);

/// Check for msg/ImuCalib message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__ImuCalib__Sequence__are_equal(const avionics_interfaces__msg__ImuCalib__Sequence * lhs, const avionics_interfaces__msg__ImuCalib__Sequence * rhs);

/// Copy an array of msg/ImuCalib messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__ImuCalib__Sequence__copy(
  const avionics_interfaces__msg__ImuCalib__Sequence * input,
  avionics_interfaces__msg__ImuCalib__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__IMU_CALIB__FUNCTIONS_H_
