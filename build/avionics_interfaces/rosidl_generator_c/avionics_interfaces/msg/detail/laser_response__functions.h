// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from avionics_interfaces:msg/LaserResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__LASER_RESPONSE__FUNCTIONS_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__LASER_RESPONSE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "avionics_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "avionics_interfaces/msg/detail/laser_response__struct.h"

/// Initialize msg/LaserResponse message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * avionics_interfaces__msg__LaserResponse
 * )) before or use
 * avionics_interfaces__msg__LaserResponse__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__LaserResponse__init(avionics_interfaces__msg__LaserResponse * msg);

/// Finalize msg/LaserResponse message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__LaserResponse__fini(avionics_interfaces__msg__LaserResponse * msg);

/// Create msg/LaserResponse message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * avionics_interfaces__msg__LaserResponse__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
avionics_interfaces__msg__LaserResponse *
avionics_interfaces__msg__LaserResponse__create();

/// Destroy msg/LaserResponse message.
/**
 * It calls
 * avionics_interfaces__msg__LaserResponse__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__LaserResponse__destroy(avionics_interfaces__msg__LaserResponse * msg);

/// Check for msg/LaserResponse message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__LaserResponse__are_equal(const avionics_interfaces__msg__LaserResponse * lhs, const avionics_interfaces__msg__LaserResponse * rhs);

/// Copy a msg/LaserResponse message.
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
avionics_interfaces__msg__LaserResponse__copy(
  const avionics_interfaces__msg__LaserResponse * input,
  avionics_interfaces__msg__LaserResponse * output);

/// Initialize array of msg/LaserResponse messages.
/**
 * It allocates the memory for the number of elements and calls
 * avionics_interfaces__msg__LaserResponse__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__LaserResponse__Sequence__init(avionics_interfaces__msg__LaserResponse__Sequence * array, size_t size);

/// Finalize array of msg/LaserResponse messages.
/**
 * It calls
 * avionics_interfaces__msg__LaserResponse__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__LaserResponse__Sequence__fini(avionics_interfaces__msg__LaserResponse__Sequence * array);

/// Create array of msg/LaserResponse messages.
/**
 * It allocates the memory for the array and calls
 * avionics_interfaces__msg__LaserResponse__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
avionics_interfaces__msg__LaserResponse__Sequence *
avionics_interfaces__msg__LaserResponse__Sequence__create(size_t size);

/// Destroy array of msg/LaserResponse messages.
/**
 * It calls
 * avionics_interfaces__msg__LaserResponse__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__LaserResponse__Sequence__destroy(avionics_interfaces__msg__LaserResponse__Sequence * array);

/// Check for msg/LaserResponse message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__LaserResponse__Sequence__are_equal(const avionics_interfaces__msg__LaserResponse__Sequence * lhs, const avionics_interfaces__msg__LaserResponse__Sequence * rhs);

/// Copy an array of msg/LaserResponse messages.
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
avionics_interfaces__msg__LaserResponse__Sequence__copy(
  const avionics_interfaces__msg__LaserResponse__Sequence * input,
  avionics_interfaces__msg__LaserResponse__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__LASER_RESPONSE__FUNCTIONS_H_
