# generated from rosidl_generator_py/resource/_idl.py.em
# with input from avionics_interfaces:msg/GyroConfigResponse.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'bias'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GyroConfigResponse(type):
    """Metaclass of message 'GyroConfigResponse'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('avionics_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'avionics_interfaces.msg.GyroConfigResponse')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__gyro_config_response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__gyro_config_response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__gyro_config_response
            cls._TYPE_SUPPORT = module.type_support_msg__msg__gyro_config_response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__gyro_config_response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GyroConfigResponse(metaclass=Metaclass_GyroConfigResponse):
    """Message class 'GyroConfigResponse'."""

    __slots__ = [
        '_id',
        '_bias',
        '_remote_command',
        '_set_bias',
        '_success',
    ]

    _fields_and_field_types = {
        'id': 'uint16',
        'bias': 'float[3]',
        'remote_command': 'boolean',
        'set_bias': 'boolean',
        'success': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 3),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.id = kwargs.get('id', int())
        if 'bias' not in kwargs:
            self.bias = numpy.zeros(3, dtype=numpy.float32)
        else:
            self.bias = numpy.array(kwargs.get('bias'), dtype=numpy.float32)
            assert self.bias.shape == (3, )
        self.remote_command = kwargs.get('remote_command', bool())
        self.set_bias = kwargs.get('set_bias', bool())
        self.success = kwargs.get('success', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.id != other.id:
            return False
        if all(self.bias != other.bias):
            return False
        if self.remote_command != other.remote_command:
            return False
        if self.set_bias != other.set_bias:
            return False
        if self.success != other.success:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property  # noqa: A003
    def id(self):  # noqa: A003
        """Message field 'id'."""
        return self._id

    @id.setter  # noqa: A003
    def id(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'id' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'id' field must be an unsigned integer in [0, 65535]"
        self._id = value

    @property
    def bias(self):
        """Message field 'bias'."""
        return self._bias

    @bias.setter
    def bias(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'bias' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 3, \
                "The 'bias' numpy.ndarray() must have a size of 3"
            self._bias = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 3 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'bias' field must be a set or sequence with length 3 and each value of type 'float'"
        self._bias = numpy.array(value, dtype=numpy.float32)

    @property
    def remote_command(self):
        """Message field 'remote_command'."""
        return self._remote_command

    @remote_command.setter
    def remote_command(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'remote_command' field must be of type 'bool'"
        self._remote_command = value

    @property
    def set_bias(self):
        """Message field 'set_bias'."""
        return self._set_bias

    @set_bias.setter
    def set_bias(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_bias' field must be of type 'bool'"
        self._set_bias = value

    @property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value
