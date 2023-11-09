// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from avionics_interfaces:msg/AccelConfigRequestMCU.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "avionics_interfaces/msg/detail/accel_config_request_mcu__struct.h"
#include "avionics_interfaces/msg/detail/accel_config_request_mcu__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool avionics_interfaces__msg__accel_config_request_mcu__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[72];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("avionics_interfaces.msg._accel_config_request_mcu.AccelConfigRequestMCU", full_classname_dest, 71) == 0);
  }
  avionics_interfaces__msg__AccelConfigRequestMCU * ros_message = _ros_message;
  {  // id
    PyObject * field = PyObject_GetAttrString(_pymsg, "id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->id = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // req_bias
    PyObject * field = PyObject_GetAttrString(_pymsg, "req_bias");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->req_bias = (Py_True == field);
    Py_DECREF(field);
  }
  {  // req_transform
    PyObject * field = PyObject_GetAttrString(_pymsg, "req_transform");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->req_transform = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * avionics_interfaces__msg__accel_config_request_mcu__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of AccelConfigRequestMCU */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("avionics_interfaces.msg._accel_config_request_mcu");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "AccelConfigRequestMCU");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  avionics_interfaces__msg__AccelConfigRequestMCU * ros_message = (avionics_interfaces__msg__AccelConfigRequestMCU *)raw_ros_message;
  {  // id
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // req_bias
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->req_bias ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "req_bias", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // req_transform
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->req_transform ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "req_transform", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
