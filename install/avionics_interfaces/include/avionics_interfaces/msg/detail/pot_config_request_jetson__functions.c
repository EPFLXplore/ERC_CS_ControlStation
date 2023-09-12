// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avionics_interfaces:msg/PotConfigRequestJetson.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/pot_config_request_jetson__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
avionics_interfaces__msg__PotConfigRequestJetson__init(avionics_interfaces__msg__PotConfigRequestJetson * msg)
{
  if (!msg) {
    return false;
  }
  // destination_id
  // min_voltages
  // max_voltages
  // min_angles
  // max_angles
  // enabled_channels
  // remote_command
  // set_min_voltages
  // set_max_voltages
  // set_min_angles
  // set_max_angles
  // set_channels_status
  return true;
}

void
avionics_interfaces__msg__PotConfigRequestJetson__fini(avionics_interfaces__msg__PotConfigRequestJetson * msg)
{
  if (!msg) {
    return;
  }
  // destination_id
  // min_voltages
  // max_voltages
  // min_angles
  // max_angles
  // enabled_channels
  // remote_command
  // set_min_voltages
  // set_max_voltages
  // set_min_angles
  // set_max_angles
  // set_channels_status
}

bool
avionics_interfaces__msg__PotConfigRequestJetson__are_equal(const avionics_interfaces__msg__PotConfigRequestJetson * lhs, const avionics_interfaces__msg__PotConfigRequestJetson * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // destination_id
  if (lhs->destination_id != rhs->destination_id) {
    return false;
  }
  // min_voltages
  for (size_t i = 0; i < 4; ++i) {
    if (lhs->min_voltages[i] != rhs->min_voltages[i]) {
      return false;
    }
  }
  // max_voltages
  for (size_t i = 0; i < 4; ++i) {
    if (lhs->max_voltages[i] != rhs->max_voltages[i]) {
      return false;
    }
  }
  // min_angles
  for (size_t i = 0; i < 4; ++i) {
    if (lhs->min_angles[i] != rhs->min_angles[i]) {
      return false;
    }
  }
  // max_angles
  for (size_t i = 0; i < 4; ++i) {
    if (lhs->max_angles[i] != rhs->max_angles[i]) {
      return false;
    }
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
  // set_min_voltages
  if (lhs->set_min_voltages != rhs->set_min_voltages) {
    return false;
  }
  // set_max_voltages
  if (lhs->set_max_voltages != rhs->set_max_voltages) {
    return false;
  }
  // set_min_angles
  if (lhs->set_min_angles != rhs->set_min_angles) {
    return false;
  }
  // set_max_angles
  if (lhs->set_max_angles != rhs->set_max_angles) {
    return false;
  }
  // set_channels_status
  if (lhs->set_channels_status != rhs->set_channels_status) {
    return false;
  }
  return true;
}

bool
avionics_interfaces__msg__PotConfigRequestJetson__copy(
  const avionics_interfaces__msg__PotConfigRequestJetson * input,
  avionics_interfaces__msg__PotConfigRequestJetson * output)
{
  if (!input || !output) {
    return false;
  }
  // destination_id
  output->destination_id = input->destination_id;
  // min_voltages
  for (size_t i = 0; i < 4; ++i) {
    output->min_voltages[i] = input->min_voltages[i];
  }
  // max_voltages
  for (size_t i = 0; i < 4; ++i) {
    output->max_voltages[i] = input->max_voltages[i];
  }
  // min_angles
  for (size_t i = 0; i < 4; ++i) {
    output->min_angles[i] = input->min_angles[i];
  }
  // max_angles
  for (size_t i = 0; i < 4; ++i) {
    output->max_angles[i] = input->max_angles[i];
  }
  // enabled_channels
  for (size_t i = 0; i < 4; ++i) {
    output->enabled_channels[i] = input->enabled_channels[i];
  }
  // remote_command
  output->remote_command = input->remote_command;
  // set_min_voltages
  output->set_min_voltages = input->set_min_voltages;
  // set_max_voltages
  output->set_max_voltages = input->set_max_voltages;
  // set_min_angles
  output->set_min_angles = input->set_min_angles;
  // set_max_angles
  output->set_max_angles = input->set_max_angles;
  // set_channels_status
  output->set_channels_status = input->set_channels_status;
  return true;
}

avionics_interfaces__msg__PotConfigRequestJetson *
avionics_interfaces__msg__PotConfigRequestJetson__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__PotConfigRequestJetson * msg = (avionics_interfaces__msg__PotConfigRequestJetson *)allocator.allocate(sizeof(avionics_interfaces__msg__PotConfigRequestJetson), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avionics_interfaces__msg__PotConfigRequestJetson));
  bool success = avionics_interfaces__msg__PotConfigRequestJetson__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avionics_interfaces__msg__PotConfigRequestJetson__destroy(avionics_interfaces__msg__PotConfigRequestJetson * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avionics_interfaces__msg__PotConfigRequestJetson__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avionics_interfaces__msg__PotConfigRequestJetson__Sequence__init(avionics_interfaces__msg__PotConfigRequestJetson__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__PotConfigRequestJetson * data = NULL;

  if (size) {
    data = (avionics_interfaces__msg__PotConfigRequestJetson *)allocator.zero_allocate(size, sizeof(avionics_interfaces__msg__PotConfigRequestJetson), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avionics_interfaces__msg__PotConfigRequestJetson__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avionics_interfaces__msg__PotConfigRequestJetson__fini(&data[i - 1]);
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
avionics_interfaces__msg__PotConfigRequestJetson__Sequence__fini(avionics_interfaces__msg__PotConfigRequestJetson__Sequence * array)
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
      avionics_interfaces__msg__PotConfigRequestJetson__fini(&array->data[i]);
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

avionics_interfaces__msg__PotConfigRequestJetson__Sequence *
avionics_interfaces__msg__PotConfigRequestJetson__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__PotConfigRequestJetson__Sequence * array = (avionics_interfaces__msg__PotConfigRequestJetson__Sequence *)allocator.allocate(sizeof(avionics_interfaces__msg__PotConfigRequestJetson__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avionics_interfaces__msg__PotConfigRequestJetson__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avionics_interfaces__msg__PotConfigRequestJetson__Sequence__destroy(avionics_interfaces__msg__PotConfigRequestJetson__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avionics_interfaces__msg__PotConfigRequestJetson__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avionics_interfaces__msg__PotConfigRequestJetson__Sequence__are_equal(const avionics_interfaces__msg__PotConfigRequestJetson__Sequence * lhs, const avionics_interfaces__msg__PotConfigRequestJetson__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avionics_interfaces__msg__PotConfigRequestJetson__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avionics_interfaces__msg__PotConfigRequestJetson__Sequence__copy(
  const avionics_interfaces__msg__PotConfigRequestJetson__Sequence * input,
  avionics_interfaces__msg__PotConfigRequestJetson__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avionics_interfaces__msg__PotConfigRequestJetson);
    avionics_interfaces__msg__PotConfigRequestJetson * data =
      (avionics_interfaces__msg__PotConfigRequestJetson *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avionics_interfaces__msg__PotConfigRequestJetson__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          avionics_interfaces__msg__PotConfigRequestJetson__fini(&data[i]);
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
    if (!avionics_interfaces__msg__PotConfigRequestJetson__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
