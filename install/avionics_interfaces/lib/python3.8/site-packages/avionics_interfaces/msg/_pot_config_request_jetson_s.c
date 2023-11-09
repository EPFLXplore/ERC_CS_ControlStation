// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from avionics_interfaces:msg/PotConfigRequestJetson.idl
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
#include "avionics_interfaces/msg/detail/pot_config_request_jetson__struct.h"
#include "avionics_interfaces/msg/detail/pot_config_request_jetson__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool avionics_interfaces__msg__pot_config_request_jetson__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[74];
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
    assert(strncmp("avionics_interfaces.msg._pot_config_request_jetson.PotConfigRequestJetson", full_classname_dest, 73) == 0);
  }
  avionics_interfaces__msg__PotConfigRequestJetson * ros_message = _ros_message;
  {  // destination_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "destination_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->destination_id = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // min_voltages
    PyObject * field = PyObject_GetAttrString(_pymsg, "min_voltages");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
      Py_ssize_t size = 4;
      float * dest = ros_message->min_voltages;
      for (Py_ssize_t i = 0; i < size; ++i) {
        float tmp = *(npy_float32 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(float));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // max_voltages
    PyObject * field = PyObject_GetAttrString(_pymsg, "max_voltages");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
      Py_ssize_t size = 4;
      float * dest = ros_message->max_voltages;
      for (Py_ssize_t i = 0; i < size; ++i) {
        float tmp = *(npy_float32 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(float));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // min_angles
    PyObject * field = PyObject_GetAttrString(_pymsg, "min_angles");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
      Py_ssize_t size = 4;
      float * dest = ros_message->min_angles;
      for (Py_ssize_t i = 0; i < size; ++i) {
        float tmp = *(npy_float32 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(float));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // max_angles
    PyObject * field = PyObject_GetAttrString(_pymsg, "max_angles");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
      Py_ssize_t size = 4;
      float * dest = ros_message->max_angles;
      for (Py_ssize_t i = 0; i < size; ++i) {
        float tmp = *(npy_float32 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(float));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // enabled_channels
    PyObject * field = PyObject_GetAttrString(_pymsg, "enabled_channels");
    if (!field) {
      return false;
    }
    {
      PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'enabled_channels'");
      if (!seq_field) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = 4;
      bool * dest = ros_message->enabled_channels;
      for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
        if (!item) {
          Py_DECREF(seq_field);
          Py_DECREF(field);
          return false;
        }
        assert(PyBool_Check(item));
        bool tmp = (item == Py_True);
        memcpy(&dest[i], &tmp, sizeof(bool));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // remote_command
    PyObject * field = PyObject_GetAttrString(_pymsg, "remote_command");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->remote_command = (Py_True == field);
    Py_DECREF(field);
  }
  {  // set_min_voltages
    PyObject * field = PyObject_GetAttrString(_pymsg, "set_min_voltages");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->set_min_voltages = (Py_True == field);
    Py_DECREF(field);
  }
  {  // set_max_voltages
    PyObject * field = PyObject_GetAttrString(_pymsg, "set_max_voltages");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->set_max_voltages = (Py_True == field);
    Py_DECREF(field);
  }
  {  // set_min_angles
    PyObject * field = PyObject_GetAttrString(_pymsg, "set_min_angles");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->set_min_angles = (Py_True == field);
    Py_DECREF(field);
  }
  {  // set_max_angles
    PyObject * field = PyObject_GetAttrString(_pymsg, "set_max_angles");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->set_max_angles = (Py_True == field);
    Py_DECREF(field);
  }
  {  // set_channels_status
    PyObject * field = PyObject_GetAttrString(_pymsg, "set_channels_status");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->set_channels_status = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * avionics_interfaces__msg__pot_config_request_jetson__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of PotConfigRequestJetson */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("avionics_interfaces.msg._pot_config_request_jetson");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "PotConfigRequestJetson");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  avionics_interfaces__msg__PotConfigRequestJetson * ros_message = (avionics_interfaces__msg__PotConfigRequestJetson *)raw_ros_message;
  {  // destination_id
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->destination_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "destination_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // min_voltages
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "min_voltages");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
    assert(sizeof(npy_float32) == sizeof(float));
    npy_float32 * dst = (npy_float32 *)PyArray_GETPTR1(seq_field, 0);
    float * src = &(ros_message->min_voltages[0]);
    memcpy(dst, src, 4 * sizeof(float));
    Py_DECREF(field);
  }
  {  // max_voltages
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "max_voltages");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
    assert(sizeof(npy_float32) == sizeof(float));
    npy_float32 * dst = (npy_float32 *)PyArray_GETPTR1(seq_field, 0);
    float * src = &(ros_message->max_voltages[0]);
    memcpy(dst, src, 4 * sizeof(float));
    Py_DECREF(field);
  }
  {  // min_angles
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "min_angles");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
    assert(sizeof(npy_float32) == sizeof(float));
    npy_float32 * dst = (npy_float32 *)PyArray_GETPTR1(seq_field, 0);
    float * src = &(ros_message->min_angles[0]);
    memcpy(dst, src, 4 * sizeof(float));
    Py_DECREF(field);
  }
  {  // max_angles
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "max_angles");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT32);
    assert(sizeof(npy_float32) == sizeof(float));
    npy_float32 * dst = (npy_float32 *)PyArray_GETPTR1(seq_field, 0);
    float * src = &(ros_message->max_angles[0]);
    memcpy(dst, src, 4 * sizeof(float));
    Py_DECREF(field);
  }
  {  // enabled_channels
    PyObject * field = NULL;
    size_t size = 4;
    bool * src = ros_message->enabled_channels;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    for (size_t i = 0; i < size; ++i) {
      int rc = PyList_SetItem(field, i, PyBool_FromLong(src[i] ? 1 : 0));
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "enabled_channels", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // remote_command
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->remote_command ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "remote_command", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // set_min_voltages
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->set_min_voltages ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "set_min_voltages", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // set_max_voltages
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->set_max_voltages ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "set_max_voltages", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // set_min_angles
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->set_min_angles ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "set_min_angles", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // set_max_angles
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->set_max_angles ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "set_max_angles", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // set_channels_status
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->set_channels_status ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "set_channels_status", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
