// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avionics_interfaces:msg/Mag.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/mag__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `mag_raw`
// Member `mag_cal`
#include "sensor_msgs/msg/detail/magnetic_field__functions.h"

bool
avionics_interfaces__msg__Mag__init(avionics_interfaces__msg__Mag * msg)
{
  if (!msg) {
    return false;
  }
  // id
  // mag_raw
  if (!sensor_msgs__msg__MagneticField__init(&msg->mag_raw)) {
    avionics_interfaces__msg__Mag__fini(msg);
    return false;
  }
  // mag_cal
  if (!sensor_msgs__msg__MagneticField__init(&msg->mag_cal)) {
    avionics_interfaces__msg__Mag__fini(msg);
    return false;
  }
  return true;
}

void
avionics_interfaces__msg__Mag__fini(avionics_interfaces__msg__Mag * msg)
{
  if (!msg) {
    return;
  }
  // id
  // mag_raw
  sensor_msgs__msg__MagneticField__fini(&msg->mag_raw);
  // mag_cal
  sensor_msgs__msg__MagneticField__fini(&msg->mag_cal);
}

bool
avionics_interfaces__msg__Mag__are_equal(const avionics_interfaces__msg__Mag * lhs, const avionics_interfaces__msg__Mag * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // id
  if (lhs->id != rhs->id) {
    return false;
  }
  // mag_raw
  if (!sensor_msgs__msg__MagneticField__are_equal(
      &(lhs->mag_raw), &(rhs->mag_raw)))
  {
    return false;
  }
  // mag_cal
  if (!sensor_msgs__msg__MagneticField__are_equal(
      &(lhs->mag_cal), &(rhs->mag_cal)))
  {
    return false;
  }
  return true;
}

bool
avionics_interfaces__msg__Mag__copy(
  const avionics_interfaces__msg__Mag * input,
  avionics_interfaces__msg__Mag * output)
{
  if (!input || !output) {
    return false;
  }
  // id
  output->id = input->id;
  // mag_raw
  if (!sensor_msgs__msg__MagneticField__copy(
      &(input->mag_raw), &(output->mag_raw)))
  {
    return false;
  }
  // mag_cal
  if (!sensor_msgs__msg__MagneticField__copy(
      &(input->mag_cal), &(output->mag_cal)))
  {
    return false;
  }
  return true;
}

avionics_interfaces__msg__Mag *
avionics_interfaces__msg__Mag__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__Mag * msg = (avionics_interfaces__msg__Mag *)allocator.allocate(sizeof(avionics_interfaces__msg__Mag), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avionics_interfaces__msg__Mag));
  bool success = avionics_interfaces__msg__Mag__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avionics_interfaces__msg__Mag__destroy(avionics_interfaces__msg__Mag * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avionics_interfaces__msg__Mag__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avionics_interfaces__msg__Mag__Sequence__init(avionics_interfaces__msg__Mag__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__Mag * data = NULL;

  if (size) {
    data = (avionics_interfaces__msg__Mag *)allocator.zero_allocate(size, sizeof(avionics_interfaces__msg__Mag), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avionics_interfaces__msg__Mag__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avionics_interfaces__msg__Mag__fini(&data[i - 1]);
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
avionics_interfaces__msg__Mag__Sequence__fini(avionics_interfaces__msg__Mag__Sequence * array)
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
      avionics_interfaces__msg__Mag__fini(&array->data[i]);
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

avionics_interfaces__msg__Mag__Sequence *
avionics_interfaces__msg__Mag__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__Mag__Sequence * array = (avionics_interfaces__msg__Mag__Sequence *)allocator.allocate(sizeof(avionics_interfaces__msg__Mag__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avionics_interfaces__msg__Mag__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avionics_interfaces__msg__Mag__Sequence__destroy(avionics_interfaces__msg__Mag__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avionics_interfaces__msg__Mag__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avionics_interfaces__msg__Mag__Sequence__are_equal(const avionics_interfaces__msg__Mag__Sequence * lhs, const avionics_interfaces__msg__Mag__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avionics_interfaces__msg__Mag__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avionics_interfaces__msg__Mag__Sequence__copy(
  const avionics_interfaces__msg__Mag__Sequence * input,
  avionics_interfaces__msg__Mag__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avionics_interfaces__msg__Mag);
    avionics_interfaces__msg__Mag * data =
      (avionics_interfaces__msg__Mag *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avionics_interfaces__msg__Mag__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          avionics_interfaces__msg__Mag__fini(&data[i]);
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
    if (!avionics_interfaces__msg__Mag__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
