// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avionics_interfaces:msg/MagConfigRequestJetson.idl
// generated code does not contain a copyright notice
#include "avionics_interfaces/msg/detail/mag_config_request_jetson__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
avionics_interfaces__msg__MagConfigRequestJetson__init(avionics_interfaces__msg__MagConfigRequestJetson * msg)
{
  if (!msg) {
    return false;
  }
  // destination_id
  // hard_iron
  // soft_iron
  // remote_command
  // set_hard_iron
  // set_soft_iron
  return true;
}

void
avionics_interfaces__msg__MagConfigRequestJetson__fini(avionics_interfaces__msg__MagConfigRequestJetson * msg)
{
  if (!msg) {
    return;
  }
  // destination_id
  // hard_iron
  // soft_iron
  // remote_command
  // set_hard_iron
  // set_soft_iron
}

bool
avionics_interfaces__msg__MagConfigRequestJetson__are_equal(const avionics_interfaces__msg__MagConfigRequestJetson * lhs, const avionics_interfaces__msg__MagConfigRequestJetson * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // destination_id
  if (lhs->destination_id != rhs->destination_id) {
    return false;
  }
  // hard_iron
  for (size_t i = 0; i < 3; ++i) {
    if (lhs->hard_iron[i] != rhs->hard_iron[i]) {
      return false;
    }
  }
  // soft_iron
  for (size_t i = 0; i < 9; ++i) {
    if (lhs->soft_iron[i] != rhs->soft_iron[i]) {
      return false;
    }
  }
  // remote_command
  if (lhs->remote_command != rhs->remote_command) {
    return false;
  }
  // set_hard_iron
  if (lhs->set_hard_iron != rhs->set_hard_iron) {
    return false;
  }
  // set_soft_iron
  if (lhs->set_soft_iron != rhs->set_soft_iron) {
    return false;
  }
  return true;
}

bool
avionics_interfaces__msg__MagConfigRequestJetson__copy(
  const avionics_interfaces__msg__MagConfigRequestJetson * input,
  avionics_interfaces__msg__MagConfigRequestJetson * output)
{
  if (!input || !output) {
    return false;
  }
  // destination_id
  output->destination_id = input->destination_id;
  // hard_iron
  for (size_t i = 0; i < 3; ++i) {
    output->hard_iron[i] = input->hard_iron[i];
  }
  // soft_iron
  for (size_t i = 0; i < 9; ++i) {
    output->soft_iron[i] = input->soft_iron[i];
  }
  // remote_command
  output->remote_command = input->remote_command;
  // set_hard_iron
  output->set_hard_iron = input->set_hard_iron;
  // set_soft_iron
  output->set_soft_iron = input->set_soft_iron;
  return true;
}

avionics_interfaces__msg__MagConfigRequestJetson *
avionics_interfaces__msg__MagConfigRequestJetson__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__MagConfigRequestJetson * msg = (avionics_interfaces__msg__MagConfigRequestJetson *)allocator.allocate(sizeof(avionics_interfaces__msg__MagConfigRequestJetson), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avionics_interfaces__msg__MagConfigRequestJetson));
  bool success = avionics_interfaces__msg__MagConfigRequestJetson__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avionics_interfaces__msg__MagConfigRequestJetson__destroy(avionics_interfaces__msg__MagConfigRequestJetson * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avionics_interfaces__msg__MagConfigRequestJetson__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avionics_interfaces__msg__MagConfigRequestJetson__Sequence__init(avionics_interfaces__msg__MagConfigRequestJetson__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__MagConfigRequestJetson * data = NULL;

  if (size) {
    data = (avionics_interfaces__msg__MagConfigRequestJetson *)allocator.zero_allocate(size, sizeof(avionics_interfaces__msg__MagConfigRequestJetson), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avionics_interfaces__msg__MagConfigRequestJetson__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avionics_interfaces__msg__MagConfigRequestJetson__fini(&data[i - 1]);
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
avionics_interfaces__msg__MagConfigRequestJetson__Sequence__fini(avionics_interfaces__msg__MagConfigRequestJetson__Sequence * array)
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
      avionics_interfaces__msg__MagConfigRequestJetson__fini(&array->data[i]);
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

avionics_interfaces__msg__MagConfigRequestJetson__Sequence *
avionics_interfaces__msg__MagConfigRequestJetson__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avionics_interfaces__msg__MagConfigRequestJetson__Sequence * array = (avionics_interfaces__msg__MagConfigRequestJetson__Sequence *)allocator.allocate(sizeof(avionics_interfaces__msg__MagConfigRequestJetson__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avionics_interfaces__msg__MagConfigRequestJetson__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avionics_interfaces__msg__MagConfigRequestJetson__Sequence__destroy(avionics_interfaces__msg__MagConfigRequestJetson__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avionics_interfaces__msg__MagConfigRequestJetson__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avionics_interfaces__msg__MagConfigRequestJetson__Sequence__are_equal(const avionics_interfaces__msg__MagConfigRequestJetson__Sequence * lhs, const avionics_interfaces__msg__MagConfigRequestJetson__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avionics_interfaces__msg__MagConfigRequestJetson__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avionics_interfaces__msg__MagConfigRequestJetson__Sequence__copy(
  const avionics_interfaces__msg__MagConfigRequestJetson__Sequence * input,
  avionics_interfaces__msg__MagConfigRequestJetson__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avionics_interfaces__msg__MagConfigRequestJetson);
    avionics_interfaces__msg__MagConfigRequestJetson * data =
      (avionics_interfaces__msg__MagConfigRequestJetson *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avionics_interfaces__msg__MagConfigRequestJetson__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          avionics_interfaces__msg__MagConfigRequestJetson__fini(&data[i]);
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
    if (!avionics_interfaces__msg__MagConfigRequestJetson__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
