// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from xplore_interfaces:msg/CameraError.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__FUNCTIONS_H_
#define XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "xplore_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "xplore_interfaces/msg/detail/camera_error__struct.h"

/// Initialize msg/CameraError message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * xplore_interfaces__msg__CameraError
 * )) before or use
 * xplore_interfaces__msg__CameraError__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
bool
xplore_interfaces__msg__CameraError__init(xplore_interfaces__msg__CameraError * msg);

/// Finalize msg/CameraError message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
void
xplore_interfaces__msg__CameraError__fini(xplore_interfaces__msg__CameraError * msg);

/// Create msg/CameraError message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * xplore_interfaces__msg__CameraError__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
xplore_interfaces__msg__CameraError *
xplore_interfaces__msg__CameraError__create();

/// Destroy msg/CameraError message.
/**
 * It calls
 * xplore_interfaces__msg__CameraError__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
void
xplore_interfaces__msg__CameraError__destroy(xplore_interfaces__msg__CameraError * msg);

/// Check for msg/CameraError message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
bool
xplore_interfaces__msg__CameraError__are_equal(const xplore_interfaces__msg__CameraError * lhs, const xplore_interfaces__msg__CameraError * rhs);

/// Copy a msg/CameraError message.
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
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
bool
xplore_interfaces__msg__CameraError__copy(
  const xplore_interfaces__msg__CameraError * input,
  xplore_interfaces__msg__CameraError * output);

/// Initialize array of msg/CameraError messages.
/**
 * It allocates the memory for the number of elements and calls
 * xplore_interfaces__msg__CameraError__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
bool
xplore_interfaces__msg__CameraError__Sequence__init(xplore_interfaces__msg__CameraError__Sequence * array, size_t size);

/// Finalize array of msg/CameraError messages.
/**
 * It calls
 * xplore_interfaces__msg__CameraError__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
void
xplore_interfaces__msg__CameraError__Sequence__fini(xplore_interfaces__msg__CameraError__Sequence * array);

/// Create array of msg/CameraError messages.
/**
 * It allocates the memory for the array and calls
 * xplore_interfaces__msg__CameraError__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
xplore_interfaces__msg__CameraError__Sequence *
xplore_interfaces__msg__CameraError__Sequence__create(size_t size);

/// Destroy array of msg/CameraError messages.
/**
 * It calls
 * xplore_interfaces__msg__CameraError__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
void
xplore_interfaces__msg__CameraError__Sequence__destroy(xplore_interfaces__msg__CameraError__Sequence * array);

/// Check for msg/CameraError message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
bool
xplore_interfaces__msg__CameraError__Sequence__are_equal(const xplore_interfaces__msg__CameraError__Sequence * lhs, const xplore_interfaces__msg__CameraError__Sequence * rhs);

/// Copy an array of msg/CameraError messages.
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
ROSIDL_GENERATOR_C_PUBLIC_xplore_interfaces
bool
xplore_interfaces__msg__CameraError__Sequence__copy(
  const xplore_interfaces__msg__CameraError__Sequence * input,
  xplore_interfaces__msg__CameraError__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__FUNCTIONS_H_
