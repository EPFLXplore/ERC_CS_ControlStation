// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avionics_interfaces:msg/MassConfigResponse.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/mass_config_response__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
avionics_interfaces__msg__MassConfigResponse__init(avionics_interfaces__msg__MassConfigResponse * msg)
{
  if (!msg) {
    return false;
  }
  // id
  // offset
  // scale
  // alpha
  // enabled_channels
  // remote_command
  // set_offset
  // set_scale
  // set_alpha
  // set_channels_status
  // success
  return true;
}

void
avionics_interfaces__msg__MassConfigResponse__fini(avionics_interfaces__msg__MassConfigResponse * msg)
{
  if (!msg) {
    return;
  }
  // id
  // offset
  // scale
  // alpha
  // enabled_channels
  // remote_command
  // set_offset
  // set_scale
  // set_alpha
  // set_channels_status
  // success
}

bool
avionics_interfaces__msg__MassConfigResponse__are_equal(const avionics_interfaces__msg__MassConfigResponse * lhs, const avionics_interfaces__msg__MassConfigResponse * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // id
  if (lhs->id != rhs->id) {
    return false;
  }
  // offset
  for (size_t i = 0; i < 4; ++i) {
    if (lhs->offset[i] != rhs->offset[i]) {
      return false;
    }
  }
  // scale
  for (size_t i = 0; i < 4; ++i) {
    if (lhs->scale[i] != rhs->scale[i]) {
      return false;
    }
  }
  // alpha
  if (lhs->alpha != rhs->alpha) {
    return false;
  }
  // enabled_channels
  for (size_t i = 0; i < 4; ++i) {
    if (lhs->enabled_channels[i] != rhs->enabled_channels[i]) {
      return false;
    }
  }
  // remote_command
  if (lhs->remote_command != rhs->remote_command) {
    return false;
  }
  // set_offset
  if (lhs->set_offset != rhs->set_offset) {
    return false;
  }
  // set_scale
  if (lhs->set_scale != rhs->set_scale) {
    return false;
  }
  // set_alpha
  if (lhs->set_alpha != rhs->set_alpha) {
    return false;
  }
  // set_channels_status
  if (lhs->set_channels_status != rhs->set_channels_status) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
avionics_interfaces__msg__MassConfigResponse__copy(
  const avionics_interfaces__msg__MassConfigResponse * input,
  avionics_interfaces__msg__MassConfigResponse * output)
{
  if (!input || !output) {
    return false;
  }
  // id
  output->id = input->id;
  // offset
  for (size_t i = 0; i < 4; ++i) {
    output->offset[i] = input->offset[i];
  }
  // scale
  for (size_t i = 0; i < 4; ++i) {
    output->scale[i] = input->scale[i];
  }
  // alpha
  output->alpha = input->alpha;
  // enabled_channels
  for (size_t i = 0; i < 4; ++i) {
    output->enabled_channels[i] = input->enabled_channels[i];
  }
  // remote_command
  output->remote_command = input->remote_command;
  // set_offset
  output->set_offset = input->set_offset;
  // set_scale
  output->set_scale = input->set_scale;
  // set_alpha
  output->set_alpha = input->set_alpha;
  // set_channels_status
  output->set_channels_status = input->set_channels_status;
  // success
  output->success = input->success;
  return true;
}

avionics_interfaces__msg__MassConfigResponse *
avionics_interfaces__msg__MassConfigResponse__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__MassConfigResponse * msg = (avionics_interfaces__msg__MassConfigResponse *)allocator.allocate(sizeof(avionics_interfaces__msg__MassConfigResponse), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avionics_interfaces__msg__MassConfigResponse));
  bool success = avionics_interfaces__msg__MassConfigResponse__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avionics_interfaces__msg__MassConfigResponse__destroy(avionics_interfaces__msg__MassConfigResponse * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avionics_interfaces__msg__MassConfigResponse__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avionics_interfaces__msg__MassConfigResponse__Sequence__init(avionics_interfaces__msg__MassConfigResponse__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__MassConfigResponse * data = NULL;

  if (size) {
    data = (avionics_interfaces__msg__MassConfigResponse *)allocator.zero_allocate(size, sizeof(avionics_interfaces__msg__MassConfigResponse), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avionics_interfaces__msg__MassConfigResponse__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avionics_interfaces__msg__MassConfigResponse__fini(&data[i - 1]);
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
avionics_interfaces__msg__MassConfigResponse__Sequence__fini(avionics_interfaces__msg__MassConfigResponse__Sequence * array)
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
      avionics_interfaces__msg__MassConfigResponse__fini(&array->data[i]);
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

avionics_interfaces__msg__MassConfigResponse__Sequence *
avionics_interfaces__msg__MassConfigResponse__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__MassConfigResponse__Sequence * array = (avionics_interfaces__msg__MassConfigResponse__Sequence *)allocator.allocate(sizeof(avionics_interfaces__msg__MassConfigResponse__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avionics_interfaces__msg__MassConfigResponse__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avionics_interfaces__msg__MassConfigResponse__Sequence__destroy(avionics_interfaces__msg__MassConfigResponse__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avionics_interfaces__msg__MassConfigResponse__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avionics_interfaces__msg__MassConfigResponse__Sequence__are_equal(const avionics_interfaces__msg__MassConfigResponse__Sequence * lhs, const avionics_interfaces__msg__MassConfigResponse__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avionics_interfaces__msg__MassConfigResponse__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avionics_interfaces__msg__MassConfigResponse__Sequence__copy(
  const avionics_interfaces__msg__MassConfigResponse__Sequence * input,
  avionics_interfaces__msg__MassConfigResponse__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avionics_interfaces__msg__MassConfigResponse);
    avionics_interfaces__msg__MassConfigResponse * data =
      (avionics_interfaces__msg__MassConfigResponse *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avionics_interfaces__msg__MassConfigResponse__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          avionics_interfaces__msg__MassConfigResponse__fini(&data[i]);
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
    if (!avionics_interfaces__msg__MassConfigResponse__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
