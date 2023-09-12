// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avionics_interfaces:msg/AccelConfigRequestJetson.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/accel_config_request_jetson__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
avionics_interfaces__msg__AccelConfigRequestJetson__init(avionics_interfaces__msg__AccelConfigRequestJetson * msg)
{
  if (!msg) {
    return false;
  }
  // destination_id
  // bias
  // transform
  // remote_command
  // set_bias
  // set_transform
  return true;
}

void
avionics_interfaces__msg__AccelConfigRequestJetson__fini(avionics_interfaces__msg__AccelConfigRequestJetson * msg)
{
  if (!msg) {
    return;
  }
  // destination_id
  // bias
  // transform
  // remote_command
  // set_bias
  // set_transform
}

bool
avionics_interfaces__msg__AccelConfigRequestJetson__are_equal(const avionics_interfaces__msg__AccelConfigRequestJetson * lhs, const avionics_interfaces__msg__AccelConfigRequestJetson * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // destination_id
  if (lhs->destination_id != rhs->destination_id) {
    return false;
  }
  // bias
  for (size_t i = 0; i < 3; ++i) {
    if (lhs->bias[i] != rhs->bias[i]) {
      return false;
    }
  }
  // transform
  for (size_t i = 0; i < 9; ++i) {
    if (lhs->transform[i] != rhs->transform[i]) {
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
  // set_transform
  if (lhs->set_transform != rhs->set_transform) {
    return false;
  }
  return true;
}

bool
avionics_interfaces__msg__AccelConfigRequestJetson__copy(
  const avionics_interfaces__msg__AccelConfigRequestJetson * input,
  avionics_interfaces__msg__AccelConfigRequestJetson * output)
{
  if (!input || !output) {
    return false;
  }
  // destination_id
  output->destination_id = input->destination_id;
  // bias
  for (size_t i = 0; i < 3; ++i) {
    output->bias[i] = input->bias[i];
  }
  // transform
  for (size_t i = 0; i < 9; ++i) {
    output->transform[i] = input->transform[i];
  }
  // remote_command
  output->remote_command = input->remote_command;
  // set_bias
  output->set_bias = input->set_bias;
  // set_transform
  output->set_transform = input->set_transform;
  return true;
}

avionics_interfaces__msg__AccelConfigRequestJetson *
avionics_interfaces__msg__AccelConfigRequestJetson__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__AccelConfigRequestJetson * msg = (avionics_interfaces__msg__AccelConfigRequestJetson *)allocator.allocate(sizeof(avionics_interfaces__msg__AccelConfigRequestJetson), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avionics_interfaces__msg__AccelConfigRequestJetson));
  bool success = avionics_interfaces__msg__AccelConfigRequestJetson__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avionics_interfaces__msg__AccelConfigRequestJetson__destroy(avionics_interfaces__msg__AccelConfigRequestJetson * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avionics_interfaces__msg__AccelConfigRequestJetson__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avionics_interfaces__msg__AccelConfigRequestJetson__Sequence__init(avionics_interfaces__msg__AccelConfigRequestJetson__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__AccelConfigRequestJetson * data = NULL;

  if (size) {
    data = (avionics_interfaces__msg__AccelConfigRequestJetson *)allocator.zero_allocate(size, sizeof(avionics_interfaces__msg__AccelConfigRequestJetson), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avionics_interfaces__msg__AccelConfigRequestJetson__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avionics_interfaces__msg__AccelConfigRequestJetson__fini(&data[i - 1]);
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
avionics_interfaces__msg__AccelConfigRequestJetson__Sequence__fini(avionics_interfaces__msg__AccelConfigRequestJetson__Sequence * array)
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
      avionics_interfaces__msg__AccelConfigRequestJetson__fini(&array->data[i]);
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

avionics_interfaces__msg__AccelConfigRequestJetson__Sequence *
avionics_interfaces__msg__AccelConfigRequestJetson__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__AccelConfigRequestJetson__Sequence * array = (avionics_interfaces__msg__AccelConfigRequestJetson__Sequence *)allocator.allocate(sizeof(avionics_interfaces__msg__AccelConfigRequestJetson__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avionics_interfaces__msg__AccelConfigRequestJetson__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avionics_interfaces__msg__AccelConfigRequestJetson__Sequence__destroy(avionics_interfaces__msg__AccelConfigRequestJetson__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avionics_interfaces__msg__AccelConfigRequestJetson__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avionics_interfaces__msg__AccelConfigRequestJetson__Sequence__are_equal(const avionics_interfaces__msg__AccelConfigRequestJetson__Sequence * lhs, const avionics_interfaces__msg__AccelConfigRequestJetson__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avionics_interfaces__msg__AccelConfigRequestJetson__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avionics_interfaces__msg__AccelConfigRequestJetson__Sequence__copy(
  const avionics_interfaces__msg__AccelConfigRequestJetson__Sequence * input,
  avionics_interfaces__msg__AccelConfigRequestJetson__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avionics_interfaces__msg__AccelConfigRequestJetson);
    avionics_interfaces__msg__AccelConfigRequestJetson * data =
      (avionics_interfaces__msg__AccelConfigRequestJetson *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avionics_interfaces__msg__AccelConfigRequestJetson__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          avionics_interfaces__msg__AccelConfigRequestJetson__fini(&data[i]);
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
    if (!avionics_interfaces__msg__AccelConfigRequestJetson__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
