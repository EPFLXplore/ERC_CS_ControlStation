// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from xplore_interfaces:msg/CameraError.idl
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
#include "xplore_interfaces/msg/detail/camera_error__struct.h"
#include "xplore_interfaces/msg/detail/camera_error__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool xplore_interfaces__msg__camera_error__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[48];
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
    assert(strncmp("xplore_interfaces.msg._camera_error.CameraError", full_classname_dest, 47) == 0);
  }
  xplore_interfaces__msg__CameraError * ros_message = _ros_message;
  {  // index
    PyObject * field = PyObject_GetAttrString(_pymsg, "index");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->index = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // ip_adresse
    PyObject * field = PyObject_GetAttrString(_pymsg, "ip_adresse");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ip_adresse = PyLong_AsLongLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * xplore_interfaces__msg__camera_error__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of CameraError */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("xplore_interfaces.msg._camera_error");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "CameraError");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  xplore_interfaces__msg__CameraError * ros_message = (xplore_interfaces__msg__CameraError *)raw_ros_message;
  {  // index
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->index);
    {
      int rc = PyObject_SetAttrString(_pymessage, "index", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ip_adresse
    PyObject * field = NULL;
    field = PyLong_FromLongLong(ros_message->ip_adresse);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ip_adresse", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
