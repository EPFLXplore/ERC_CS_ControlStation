// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avionics_interfaces:msg/PotConfigRequestMCU.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/pot_config_request_mcu__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
avionics_interfaces__msg__PotConfigRequestMCU__init(avionics_interfaces__msg__PotConfigRequestMCU * msg)
{
  if (!msg) {
    return false;
  }
  // id
  // req_min_voltages
  // req_max_voltages
  // req_min_angles
  // req_max_angles
  // req_channels_status
  return true;
}

void
avionics_interfaces__msg__PotConfigRequestMCU__fini(avionics_interfaces__msg__PotConfigRequestMCU * msg)
{
  if (!msg) {
    return;
  }
  // id
  // req_min_voltages
  // req_max_voltages
  // req_min_angles
  // req_max_angles
  // req_channels_status
}

bool
avionics_interfaces__msg__PotConfigRequestMCU__are_equal(const avionics_interfaces__msg__PotConfigRequestMCU * lhs, const avionics_interfaces__msg__PotConfigRequestMCU * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // id
  if (lhs->id != rhs->id) {
    return false;
  }
  // req_min_voltages
  if (lhs->req_min_voltages != rhs->req_min_voltages) {
    return false;
  }
  // req_max_voltages
  if (lhs->req_max_voltages != rhs->req_max_voltages) {
    return false;
  }
  // req_min_angles
  if (lhs->req_min_angles != rhs->req_min_angles) {
    return false;
  }
  // req_max_angles
  if (lhs->req_max_angles != rhs->req_max_angles) {
    return false;
  }
  // req_channels_status
  if (lhs->req_channels_status != rhs->req_channels_status) {
    return false;
  }
  return true;
}

bool
avionics_interfaces__msg__PotConfigRequestMCU__copy(
  const avionics_interfaces__msg__PotConfigRequestMCU * input,
  avionics_interfaces__msg__PotConfigRequestMCU * output)
{
  if (!input || !output) {
    return false;
  }
  // id
  output->id = input->id;
  // req_min_voltages
  output->req_min_voltages = input->req_min_voltages;
  // req_max_voltages
  output->req_max_voltages = input->req_max_voltages;
  // req_min_angles
  output->req_min_angles = input->req_min_angles;
  // req_max_angles
  output->req_max_angles = input->req_max_angles;
  // req_channels_status
  output->req_channels_status = input->req_channels_status;
  return true;
}

avionics_interfaces__msg__PotConfigRequestMCU *
avionics_interfaces__msg__PotConfigRequestMCU__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__PotConfigRequestMCU * msg = (avionics_interfaces__msg__PotConfigRequestMCU *)allocator.allocate(sizeof(avionics_interfaces__msg__PotConfigRequestMCU), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avionics_interfaces__msg__PotConfigRequestMCU));
  bool success = avionics_interfaces__msg__PotConfigRequestMCU__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avionics_interfaces__msg__PotConfigRequestMCU__destroy(avionics_interfaces__msg__PotConfigRequestMCU * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avionics_interfaces__msg__PotConfigRequestMCU__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avionics_interfaces__msg__PotConfigRequestMCU__Sequence__init(avionics_interfaces__msg__PotConfigRequestMCU__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__PotConfigRequestMCU * data = NULL;

  if (size) {
    data = (avionics_interfaces__msg__PotConfigRequestMCU *)allocator.zero_allocate(size, sizeof(avionics_interfaces__msg__PotConfigRequestMCU), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avionics_interfaces__msg__PotConfigRequestMCU__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avionics_interfaces__msg__PotConfigRequestMCU__fini(&data[i - 1]);
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
avionics_interfaces__msg__PotConfigRequestMCU__Sequence__fini(avionics_interfaces__msg__PotConfigRequestMCU__Sequence * array)
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
      avionics_interfaces__msg__PotConfigRequestMCU__fini(&array->data[i]);
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

avionics_interfaces__msg__PotConfigRequestMCU__Sequence *
avionics_interfaces__msg__PotConfigRequestMCU__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__PotConfigRequestMCU__Sequence * array = (avionics_interfaces__msg__PotConfigRequestMCU__Sequence *)allocator.allocate(sizeof(avionics_interfaces__msg__PotConfigRequestMCU__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avionics_interfaces__msg__PotConfigRequestMCU__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avionics_interfaces__msg__PotConfigRequestMCU__Sequence__destroy(avionics_interfaces__msg__PotConfigRequestMCU__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avionics_interfaces__msg__PotConfigRequestMCU__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avionics_interfaces__msg__PotConfigRequestMCU__Sequence__are_equal(const avionics_interfaces__msg__PotConfigRequestMCU__Sequence * lhs, const avionics_interfaces__msg__PotConfigRequestMCU__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avionics_interfaces__msg__PotConfigRequestMCU__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avionics_interfaces__msg__PotConfigRequestMCU__Sequence__copy(
  const avionics_interfaces__msg__PotConfigRequestMCU__Sequence * input,
  avionics_interfaces__msg__PotConfigRequestMCU__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avionics_interfaces__msg__PotConfigRequestMCU);
    avionics_interfaces__msg__PotConfigRequestMCU * data =
      (avionics_interfaces__msg__PotConfigRequestMCU *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avionics_interfaces__msg__PotConfigRequestMCU__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          avionics_interfaces__msg__PotConfigRequestMCU__fini(&data[i]);
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
    if (!avionics_interfaces__msg__PotConfigRequestMCU__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
