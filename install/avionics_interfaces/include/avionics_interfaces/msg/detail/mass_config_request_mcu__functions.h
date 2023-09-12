// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from avionics_interfaces:msg/MassConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_MCU__FUNCTIONS_H_
#define AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_MCU__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "avionics_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "avionics_interfaces/msg/detail/mass_config_request_mcu__struct.h"

/// Initialize msg/MassConfigRequestMCU message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * avionics_interfaces__msg__MassConfigRequestMCU
 * )) before or use
 * avionics_interfaces__msg__MassConfigRequestMCU__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__MassConfigRequestMCU__init(avionics_interfaces__msg__MassConfigRequestMCU * msg);

/// Finalize msg/MassConfigRequestMCU message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__MassConfigRequestMCU__fini(avionics_interfaces__msg__MassConfigRequestMCU * msg);

/// Create msg/MassConfigRequestMCU message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * avionics_interfaces__msg__MassConfigRequestMCU__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
avionics_interfaces__msg__MassConfigRequestMCU *
avionics_interfaces__msg__MassConfigRequestMCU__create();

/// Destroy msg/MassConfigRequestMCU message.
/**
 * It calls
 * avionics_interfaces__msg__MassConfigRequestMCU__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__MassConfigRequestMCU__destroy(avionics_interfaces__msg__MassConfigRequestMCU * msg);

/// Check for msg/MassConfigRequestMCU message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__MassConfigRequestMCU__are_equal(const avionics_interfaces__msg__MassConfigRequestMCU * lhs, const avionics_interfaces__msg__MassConfigRequestMCU * rhs);

/// Copy a msg/MassConfigRequestMCU message.
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
avionics_interfaces__msg__MassConfigRequestMCU__copy(
  const avionics_interfaces__msg__MassConfigRequestMCU * input,
  avionics_interfaces__msg__MassConfigRequestMCU * output);

/// Initialize array of msg/MassConfigRequestMCU messages.
/**
 * It allocates the memory for the number of elements and calls
 * avionics_interfaces__msg__MassConfigRequestMCU__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__MassConfigRequestMCU__Sequence__init(avionics_interfaces__msg__MassConfigRequestMCU__Sequence * array, size_t size);

/// Finalize array of msg/MassConfigRequestMCU messages.
/**
 * It calls
 * avionics_interfaces__msg__MassConfigRequestMCU__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__MassConfigRequestMCU__Sequence__fini(avionics_interfaces__msg__MassConfigRequestMCU__Sequence * array);

/// Create array of msg/MassConfigRequestMCU messages.
/**
 * It allocates the memory for the array and calls
 * avionics_interfaces__msg__MassConfigRequestMCU__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
avionics_interfaces__msg__MassConfigRequestMCU__Sequence *
avionics_interfaces__msg__MassConfigRequestMCU__Sequence__create(size_t size);

/// Destroy array of msg/MassConfigRequestMCU messages.
/**
 * It calls
 * avionics_interfaces__msg__MassConfigRequestMCU__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
void
avionics_interfaces__msg__MassConfigRequestMCU__Sequence__destroy(avionics_interfaces__msg__MassConfigRequestMCU__Sequence * array);

/// Check for msg/MassConfigRequestMCU message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_avionics_interfaces
bool
avionics_interfaces__msg__MassConfigRequestMCU__Sequence__are_equal(const avionics_interfaces__msg__MassConfigRequestMCU__Sequence * lhs, const avionics_interfaces__msg__MassConfigRequestMCU__Sequence * rhs);

/// Copy an array of msg/MassConfigRequestMCU messages.
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
avionics_interfaces__msg__MassConfigRequestMCU__Sequence__copy(
  const avionics_interfaces__msg__MassConfigRequestMCU__Sequence * input,
  avionics_interfaces__msg__MassConfigRequestMCU__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MASS_CONFIG_REQUEST_MCU__FUNCTIONS_H_
