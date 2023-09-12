// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avionics_interfaces:msg/MassCalibScale.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/mass_calib_scale__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
avionics_interfaces__msg__MassCalibScale__init(avionics_interfaces__msg__MassCalibScale * msg)
{
  if (!msg) {
    return false;
  }
  // destination_id
  // channel
  // expected_weight
  return true;
}

void
avionics_interfaces__msg__MassCalibScale__fini(avionics_interfaces__msg__MassCalibScale * msg)
{
  if (!msg) {
    return;
  }
  // destination_id
  // channel
  // expected_weight
}

bool
avionics_interfaces__msg__MassCalibScale__are_equal(const avionics_interfaces__msg__MassCalibScale * lhs, const avionics_interfaces__msg__MassCalibScale * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // destination_id
  if (lhs->destination_id != rhs->destination_id) {
    return false;
  }
  // channel
  if (lhs->channel != rhs->channel) {
    return false;
  }
  // expected_weight
  if (lhs->expected_weight != rhs->expected_weight) {
    return false;
  }
  return true;
}

bool
avionics_interfaces__msg__MassCalibScale__copy(
  const avionics_interfaces__msg__MassCalibScale * input,
  avionics_interfaces__msg__MassCalibScale * output)
{
  if (!input || !output) {
    return false;
  }
  // destination_id
  output->destination_id = input->destination_id;
  // channel
  output->channel = input->channel;
  // expected_weight
  output->expected_weight = input->expected_weight;
  return true;
}

avionics_interfaces__msg__MassCalibScale *
avionics_interfaces__msg__MassCalibScale__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__MassCalibScale * msg = (avionics_interfaces__msg__MassCalibScale *)allocator.allocate(sizeof(avionics_interfaces__msg__MassCalibScale), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avionics_interfaces__msg__MassCalibScale));
  bool success = avionics_interfaces__msg__MassCalibScale__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avionics_interfaces__msg__MassCalibScale__destroy(avionics_interfaces__msg__MassCalibScale * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avionics_interfaces__msg__MassCalibScale__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avionics_interfaces__msg__MassCalibScale__Sequence__init(avionics_interfaces__msg__MassCalibScale__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__MassCalibScale * data = NULL;

  if (size) {
    data = (avionics_interfaces__msg__MassCalibScale *)allocator.zero_allocate(size, sizeof(avionics_interfaces__msg__MassCalibScale), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avionics_interfaces__msg__MassCalibScale__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avionics_interfaces__msg__MassCalibScale__fini(&data[i - 1]);
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
avionics_interfaces__msg__MassCalibScale__Sequence__fini(avionics_interfaces__msg__MassCalibScale__Sequence * array)
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
      avionics_interfaces__msg__MassCalibScale__fini(&array->data[i]);
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

avionics_interfaces__msg__MassCalibScale__Sequence *
avionics_interfaces__msg__MassCalibScale__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__MassCalibScale__Sequence * array = (avionics_interfaces__msg__MassCalibScale__Sequence *)allocator.allocate(sizeof(avionics_interfaces__msg__MassCalibScale__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avionics_interfaces__msg__MassCalibScale__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avionics_interfaces__msg__MassCalibScale__Sequence__destroy(avionics_interfaces__msg__MassCalibScale__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avionics_interfaces__msg__MassCalibScale__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avionics_interfaces__msg__MassCalibScale__Sequence__are_equal(const avionics_interfaces__msg__MassCalibScale__Sequence * lhs, const avionics_interfaces__msg__MassCalibScale__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avionics_interfaces__msg__MassCalibScale__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avionics_interfaces__msg__MassCalibScale__Sequence__copy(
  const avionics_interfaces__msg__MassCalibScale__Sequence * input,
  avionics_interfaces__msg__MassCalibScale__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avionics_interfaces__msg__MassCalibScale);
    avionics_interfaces__msg__MassCalibScale * data =
      (avionics_interfaces__msg__MassCalibScale *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avionics_interfaces__msg__MassCalibScale__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          avionics_interfaces__msg__MassCalibScale__fini(&data[i]);
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
    if (!avionics_interfaces__msg__MassCalibScale__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
