// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from xplore_interfaces:srv/EnableCamera.idl
// generated code does not contain a copyright notice
#include "xplore_interfaces/srv/detail/enable_camera__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
xplore_interfaces__srv__EnableCamera_Request__init(xplore_interfaces__srv__EnableCamera_Request * msg)
{
  if (!msg) {
    return false;
  }
  // index
  return true;
}

void
xplore_interfaces__srv__EnableCamera_Request__fini(xplore_interfaces__srv__EnableCamera_Request * msg)
{
  if (!msg) {
    return;
  }
  // index
}

bool
xplore_interfaces__srv__EnableCamera_Request__are_equal(const xplore_interfaces__srv__EnableCamera_Request * lhs, const xplore_interfaces__srv__EnableCamera_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // index
  if (lhs->index != rhs->index) {
    return false;
  }
  return true;
}

bool
xplore_interfaces__srv__EnableCamera_Request__copy(
  const xplore_interfaces__srv__EnableCamera_Request * input,
  xplore_interfaces__srv__EnableCamera_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // index
  output->index = input->index;
  return true;
}

xplore_interfaces__srv__EnableCamera_Request *
xplore_interfaces__srv__EnableCamera_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  xplore_interfaces__srv__EnableCamera_Request * msg = (xplore_interfaces__srv__EnableCamera_Request *)allocator.allocate(sizeof(xplore_interfaces__srv__EnableCamera_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(xplore_interfaces__srv__EnableCamera_Request));
  bool success = xplore_interfaces__srv__EnableCamera_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
xplore_interfaces__srv__EnableCamera_Request__destroy(xplore_interfaces__srv__EnableCamera_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    xplore_interfaces__srv__EnableCamera_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
xplore_interfaces__srv__EnableCamera_Request__Sequence__init(xplore_interfaces__srv__EnableCamera_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  xplore_interfaces__srv__EnableCamera_Request * data = NULL;

  if (size) {
    data = (xplore_interfaces__srv__EnableCamera_Request *)allocator.zero_allocate(size, sizeof(xplore_interfaces__srv__EnableCamera_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = xplore_interfaces__srv__EnableCamera_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        xplore_interfaces__srv__EnableCamera_Request__fini(&data[i - 1]);
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
xplore_interfaces__srv__EnableCamera_Request__Sequence__fini(xplore_interfaces__srv__EnableCamera_Request__Sequence * array)
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
      xplore_interfaces__srv__EnableCamera_Request__fini(&array->data[i]);
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

xplore_interfaces__srv__EnableCamera_Request__Sequence *
xplore_interfaces__srv__EnableCamera_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  xplore_interfaces__srv__EnableCamera_Request__Sequence * array = (xplore_interfaces__srv__EnableCamera_Request__Sequence *)allocator.allocate(sizeof(xplore_interfaces__srv__EnableCamera_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = xplore_interfaces__srv__EnableCamera_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
xplore_interfaces__srv__EnableCamera_Request__Sequence__destroy(xplore_interfaces__srv__EnableCamera_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    xplore_interfaces__srv__EnableCamera_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
xplore_interfaces__srv__EnableCamera_Request__Sequence__are_equal(const xplore_interfaces__srv__EnableCamera_Request__Sequence * lhs, const xplore_interfaces__srv__EnableCamera_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!xplore_interfaces__srv__EnableCamera_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
xplore_interfaces__srv__EnableCamera_Request__Sequence__copy(
  const xplore_interfaces__srv__EnableCamera_Request__Sequence * input,
  xplore_interfaces__srv__EnableCamera_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(xplore_interfaces__srv__EnableCamera_Request);
    xplore_interfaces__srv__EnableCamera_Request * data =
      (xplore_interfaces__srv__EnableCamera_Request *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!xplore_interfaces__srv__EnableCamera_Request__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          xplore_interfaces__srv__EnableCamera_Request__fini(&data[i]);
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
    if (!xplore_interfaces__srv__EnableCamera_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
xplore_interfaces__srv__EnableCamera_Response__init(xplore_interfaces__srv__EnableCamera_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  // ip_adresse
  return true;
}

void
xplore_interfaces__srv__EnableCamera_Response__fini(xplore_interfaces__srv__EnableCamera_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
  // ip_adresse
}

bool
xplore_interfaces__srv__EnableCamera_Response__are_equal(const xplore_interfaces__srv__EnableCamera_Response * lhs, const xplore_interfaces__srv__EnableCamera_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // ip_adresse
  if (lhs->ip_adresse != rhs->ip_adresse) {
    return false;
  }
  return true;
}

bool
xplore_interfaces__srv__EnableCamera_Response__copy(
  const xplore_interfaces__srv__EnableCamera_Response * input,
  xplore_interfaces__srv__EnableCamera_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  // ip_adresse
  output->ip_adresse = input->ip_adresse;
  return true;
}

xplore_interfaces__srv__EnableCamera_Response *
xplore_interfaces__srv__EnableCamera_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  xplore_interfaces__srv__EnableCamera_Response * msg = (xplore_interfaces__srv__EnableCamera_Response *)allocator.allocate(sizeof(xplore_interfaces__srv__EnableCamera_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(xplore_interfaces__srv__EnableCamera_Response));
  bool success = xplore_interfaces__srv__EnableCamera_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
xplore_interfaces__srv__EnableCamera_Response__destroy(xplore_interfaces__srv__EnableCamera_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    xplore_interfaces__srv__EnableCamera_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
xplore_interfaces__srv__EnableCamera_Response__Sequence__init(xplore_interfaces__srv__EnableCamera_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  xplore_interfaces__srv__EnableCamera_Response * data = NULL;

  if (size) {
    data = (xplore_interfaces__srv__EnableCamera_Response *)allocator.zero_allocate(size, sizeof(xplore_interfaces__srv__EnableCamera_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = xplore_interfaces__srv__EnableCamera_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        xplore_interfaces__srv__EnableCamera_Response__fini(&data[i - 1]);
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
xplore_interfaces__srv__EnableCamera_Response__Sequence__fini(xplore_interfaces__srv__EnableCamera_Response__Sequence * array)
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
      xplore_interfaces__srv__EnableCamera_Response__fini(&array->data[i]);
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

xplore_interfaces__srv__EnableCamera_Response__Sequence *
xplore_interfaces__srv__EnableCamera_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  xplore_interfaces__srv__EnableCamera_Response__Sequence * array = (xplore_interfaces__srv__EnableCamera_Response__Sequence *)allocator.allocate(sizeof(xplore_interfaces__srv__EnableCamera_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = xplore_interfaces__srv__EnableCamera_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
xplore_interfaces__srv__EnableCamera_Response__Sequence__destroy(xplore_interfaces__srv__EnableCamera_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    xplore_interfaces__srv__EnableCamera_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
xplore_interfaces__srv__EnableCamera_Response__Sequence__are_equal(const xplore_interfaces__srv__EnableCamera_Response__Sequence * lhs, const xplore_interfaces__srv__EnableCamera_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!xplore_interfaces__srv__EnableCamera_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
xplore_interfaces__srv__EnableCamera_Response__Sequence__copy(
  const xplore_interfaces__srv__EnableCamera_Response__Sequence * input,
  xplore_interfaces__srv__EnableCamera_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(xplore_interfaces__srv__EnableCamera_Response);
    xplore_interfaces__srv__EnableCamera_Response * data =
      (xplore_interfaces__srv__EnableCamera_Response *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!xplore_interfaces__srv__EnableCamera_Response__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          xplore_interfaces__srv__EnableCamera_Response__fini(&data[i]);
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
    if (!xplore_interfaces__srv__EnableCamera_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
