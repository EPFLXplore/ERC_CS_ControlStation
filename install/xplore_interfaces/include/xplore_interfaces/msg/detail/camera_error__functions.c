// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from xplore_interfaces:msg/CameraError.idl
// generated code does not contain a copyright notice
#include "xplore_interfaces/msg/detail/camera_error__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
xplore_interfaces__msg__CameraError__init(xplore_interfaces__msg__CameraError * msg)
{
  if (!msg) {
    return false;
  }
  // index
  // ip_adresse
  return true;
}

void
xplore_interfaces__msg__CameraError__fini(xplore_interfaces__msg__CameraError * msg)
{
  if (!msg) {
    return;
  }
  // index
  // ip_adresse
}

bool
xplore_interfaces__msg__CameraError__are_equal(const xplore_interfaces__msg__CameraError * lhs, const xplore_interfaces__msg__CameraError * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // index
  if (lhs->index != rhs->index) {
    return false;
  }
  // ip_adresse
  if (lhs->ip_adresse != rhs->ip_adresse) {
    return false;
  }
  return true;
}

bool
xplore_interfaces__msg__CameraError__copy(
  const xplore_interfaces__msg__CameraError * input,
  xplore_interfaces__msg__CameraError * output)
{
  if (!input || !output) {
    return false;
  }
  // index
  output->index = input->index;
  // ip_adresse
  output->ip_adresse = input->ip_adresse;
  return true;
}

xplore_interfaces__msg__CameraError *
xplore_interfaces__msg__CameraError__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  xplore_interfaces__msg__CameraError * msg = (xplore_interfaces__msg__CameraError *)allocator.allocate(sizeof(xplore_interfaces__msg__CameraError), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(xplore_interfaces__msg__CameraError));
  bool success = xplore_interfaces__msg__CameraError__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
xplore_interfaces__msg__CameraError__destroy(xplore_interfaces__msg__CameraError * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    xplore_interfaces__msg__CameraError__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
xplore_interfaces__msg__CameraError__Sequence__init(xplore_interfaces__msg__CameraError__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  xplore_interfaces__msg__CameraError * data = NULL;

  if (size) {
    data = (xplore_interfaces__msg__CameraError *)allocator.zero_allocate(size, sizeof(xplore_interfaces__msg__CameraError), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = xplore_interfaces__msg__CameraError__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        xplore_interfaces__msg__CameraError__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
xplore_interfaces__msg__CameraError__Sequence__fini(xplore_interfaces__msg__CameraError__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      xplore_interfaces__msg__CameraError__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

xplore_interfaces__msg__CameraError__Sequence *
xplore_interfaces__msg__CameraError__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  xplore_interfaces__msg__CameraError__Sequence * array = (xplore_interfaces__msg__CameraError__Sequence *)allocator.allocate(sizeof(xplore_interfaces__msg__CameraError__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = xplore_interfaces__msg__CameraError__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
xplore_interfaces__msg__CameraError__Sequence__destroy(xplore_interfaces__msg__CameraError__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    xplore_interfaces__msg__CameraError__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
xplore_interfaces__msg__CameraError__Sequence__are_equal(const xplore_interfaces__msg__CameraError__Sequence * lhs, const xplore_interfaces__msg__CameraError__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!xplore_interfaces__msg__CameraError__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
xplore_interfaces__msg__CameraError__Sequence__copy(
  const xplore_interfaces__msg__CameraError__Sequence * input,
  xplore_interfaces__msg__CameraError__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(xplore_interfaces__msg__CameraError);
    xplore_interfaces__msg__CameraError * data =
      (xplore_interfaces__msg__CameraError *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!xplore_interfaces__msg__CameraError__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          xplore_interfaces__msg__CameraError__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!xplore_interfaces__msg__CameraError__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
