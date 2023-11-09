// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from avionics_interfaces:msg/Voltage.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__VOLTAGE__FUNCTIONS_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__VOLTAGE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "avionics_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "avionics_interfaces/msg/detail/voltage__struct.h"

/// Initialize msg/Voltage message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * avionics_interfaces__msg__Voltage
 * )) before or use
 * avionics_interfaces__msg__Voltage__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__Voltage__init(avionics_interfaces__msg__Voltage * msg);

/// Finalize msg/Voltage message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__Voltage__fini(avionics_interfaces__msg__Voltage * msg);

/// Create msg/Voltage message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * avionics_interfaces__msg__Voltage__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
avionics_interfaces__msg__Voltage *
avionics_interfaces__msg__Voltage__create();

/// Destroy msg/Voltage message.
/**
 * It calls
 * avionics_interfaces__msg__Voltage__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__Voltage__destroy(avionics_interfaces__msg__Voltage * msg);

/// Check for msg/Voltage message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__Voltage__are_equal(const avionics_interfaces__msg__Voltage * lhs, const avionics_interfaces__msg__Voltage * rhs);

/// Copy a msg/Voltage message.
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
avionics_interfaces__msg__Voltage__copy(
  const avionics_interfaces__msg__Voltage * input,
  avionics_interfaces__msg__Voltage * output);

/// Initialize array of msg/Voltage messages.
/**
 * It allocates the memory for the number of elements and calls
 * avionics_interfaces__msg__Voltage__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__Voltage__Sequence__init(avionics_interfaces__msg__Voltage__Sequence * array, size_t size);

/// Finalize array of msg/Voltage messages.
/**
 * It calls
 * avionics_interfaces__msg__Voltage__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__Voltage__Sequence__fini(avionics_interfaces__msg__Voltage__Sequence * array);

/// Create array of msg/Voltage messages.
/**
 * It allocates the memory for the array and calls
 * avionics_interfaces__msg__Voltage__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
avionics_interfaces__msg__Voltage__Sequence *
avionics_interfaces__msg__Voltage__Sequence__create(size_t size);

/// Destroy array of msg/Voltage messages.
/**
 * It calls
 * avionics_interfaces__msg__Voltage__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__Voltage__Sequence__destroy(avionics_interfaces__msg__Voltage__Sequence * array);

/// Check for msg/Voltage message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__Voltage__Sequence__are_equal(const avionics_interfaces__msg__Voltage__Sequence * lhs, const avionics_interfaces__msg__Voltage__Sequence * rhs);

/// Copy an array of msg/Voltage messages.
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
avionics_interfaces__msg__Voltage__Sequence__copy(
  const avionics_interfaces__msg__Voltage__Sequence * input,
  avionics_interfaces__msg__Voltage__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__VOLTAGE__FUNCTIONS_H_
