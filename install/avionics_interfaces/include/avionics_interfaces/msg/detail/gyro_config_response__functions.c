// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avionics_interfaces:msg/GyroConfigResponse.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/gyro_config_response__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
avionics_interfaces__msg__GyroConfigResponse__init(avionics_interfaces__msg__GyroConfigResponse * msg)
{
  if (!msg) {
    return false;
  }
  // id
  // bias
  // remote_command
  // set_bias
  // success
  return true;
}

void
avionics_interfaces__msg__GyroConfigResponse__fini(avionics_interfaces__msg__GyroConfigResponse * msg)
{
  if (!msg) {
    return;
  }
  // id
  // bias
  // remote_command
  // set_bias
  // success
}

bool
avionics_interfaces__msg__GyroConfigResponse__are_equal(const avionics_interfaces__msg__GyroConfigResponse * lhs, const avionics_interfaces__msg__GyroConfigResponse * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // id
  if (lhs->id != rhs->id) {
    return false;
  }
  // bias
  for (size_t i = 0; i < 3; ++i) {
    if (lhs->bias[i] != rhs->bias[i]) {
      return false;
    }
  }
  // remote_command
  if (lhs->remote_command != rhs->remote_command) {
    return false;
  }
  // set_bias
  if (lhs->set_bias != rhs->set_bias) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
avionics_interfaces__msg__GyroConfigResponse__copy(
  const avionics_interfaces__msg__GyroConfigResponse * input,
  avionics_interfaces__msg__GyroConfigResponse * output)
{
  if (!input || !output) {
    return false;
  }
  // id
  output->id = input->id;
  // bias
  for (size_t i = 0; i < 3; ++i) {
    output->bias[i] = input->bias[i];
  }
  // remote_command
  output->remote_command = input->remote_command;
  // set_bias
  output->set_bias = input->set_bias;
  // success
  output->success = input->success;
  return true;
}

avionics_interfaces__msg__GyroConfigResponse *
avionics_interfaces__msg__GyroConfigResponse__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__GyroConfigResponse * msg = (avionics_interfaces__msg__GyroConfigResponse *)allocator.allocate(sizeof(avionics_interfaces__msg__GyroConfigResponse), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avionics_interfaces__msg__GyroConfigResponse));
  bool success = avionics_interfaces__msg__GyroConfigResponse__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avionics_interfaces__msg__GyroConfigResponse__destroy(avionics_interfaces__msg__GyroConfigResponse * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avionics_interfaces__msg__GyroConfigResponse__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avionics_interfaces__msg__GyroConfigResponse__Sequence__init(avionics_interfaces__msg__GyroConfigResponse__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__GyroConfigResponse * data = NULL;

  if (size) {
    data = (avionics_interfaces__msg__GyroConfigResponse *)allocator.zero_allocate(size, sizeof(avionics_interfaces__msg__GyroConfigResponse), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avionics_interfaces__msg__GyroConfigResponse__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avionics_interfaces__msg__GyroConfigResponse__fini(&data[i - 1]);
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
avionics_interfaces__msg__GyroConfigResponse__Sequence__fini(avionics_interfaces__msg__GyroConfigResponse__Sequence * array)
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
      avionics_interfaces__msg__GyroConfigResponse__fini(&array->data[i]);
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

avionics_interfaces__msg__GyroConfigResponse__Sequence *
avionics_interfaces__msg__GyroConfigResponse__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__GyroConfigResponse__Sequence * array = (avionics_interfaces__msg__GyroConfigResponse__Sequence *)allocator.allocate(sizeof(avionics_interfaces__msg__GyroConfigResponse__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avionics_interfaces__msg__GyroConfigResponse__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avionics_interfaces__msg__GyroConfigResponse__Sequence__destroy(avionics_interfaces__msg__GyroConfigResponse__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avionics_interfaces__msg__GyroConfigResponse__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avionics_interfaces__msg__GyroConfigResponse__Sequence__are_equal(const avionics_interfaces__msg__GyroConfigResponse__Sequence * lhs, const avionics_interfaces__msg__GyroConfigResponse__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avionics_interfaces__msg__GyroConfigResponse__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avionics_interfaces__msg__GyroConfigResponse__Sequence__copy(
  const avionics_interfaces__msg__GyroConfigResponse__Sequence * input,
  avionics_interfaces__msg__GyroConfigResponse__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avionics_interfaces__msg__GyroConfigResponse);
    avionics_interfaces__msg__GyroConfigResponse * data =
      (avionics_interfaces__msg__GyroConfigResponse *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avionics_interfaces__msg__GyroConfigResponse__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          avionics_interfaces__msg__GyroConfigResponse__fini(&data[i]);
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
    if (!avionics_interfaces__msg__GyroConfigResponse__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
