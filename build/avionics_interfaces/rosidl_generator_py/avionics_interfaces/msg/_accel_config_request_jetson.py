# generated from rosidl_generator_py/resource/_idl.py.em
# with input from avionics_interfaces:msg/AccelConfigRequestJetson.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'bias'
# Member 'transform'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AccelConfigRequestJetson(type):
    """Metaclass of message 'AccelConfigRequestJetson'."""

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
                'avionics_interfaces.msg.AccelConfigRequestJetson')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__accel_config_request_jetson
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__accel_config_request_jetson
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__accel_config_request_jetson
            cls._TYPE_SUPPORT = module.type_support_msg__msg__accel_config_request_jetson
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__accel_config_request_jetson

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AccelConfigRequestJetson(metaclass=Metaclass_AccelConfigRequestJetson):
    """Message class 'AccelConfigRequestJetson'."""

    __slots__ = [
        '_destination_id',
        '_bias',
        '_transform',
        '_remote_command',
        '_set_bias',
        '_set_transform',
    ]

    _fields_and_field_types = {
        'destination_id': 'uint16',
        'bias': 'float[3]',
        'transform': 'float[9]',
        'remote_command': 'boolean',
        'set_bias': 'boolean',
        'set_transform': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 3),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 9),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.destination_id = kwargs.get('destination_id', int())
        if 'bias' not in kwargs:
            self.bias = numpy.zeros(3, dtype=numpy.float32)
        else:
            self.bias = numpy.array(kwargs.get('bias'), dtype=numpy.float32)
            assert self.bias.shape == (3, )
        if 'transform' not in kwargs:
            self.transform = numpy.zeros(9, dtype=numpy.float32)
        else:
            self.transform = numpy.array(kwargs.get('transform'), dtype=numpy.float32)
            assert self.transform.shape == (9, )
        self.remote_command = kwargs.get('remote_command', bool())
        self.set_bias = kwargs.get('set_bias', bool())
        self.set_transform = kwargs.get('set_transform', bool())

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
        if self.destination_id != other.destination_id:
            return False
        if all(self.bias != other.bias):
            return False
        if all(self.transform != other.transform):
            return False
        if self.remote_command != other.remote_command:
            return False
        if self.set_bias != other.set_bias:
            return False
        if self.set_transform != other.set_transform:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def destination_id(self):
        """Message field 'destination_id'."""
        return self._destination_id

    @destination_id.setter
    def destination_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'destination_id' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'destination_id' field must be an unsigned integer in [0, 65535]"
        self._destination_id = value

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
    def transform(self):
        """Message field 'transform'."""
        return self._transform

    @transform.setter
    def transform(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'transform' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 9, \
                "The 'transform' numpy.ndarray() must have a size of 9"
            self._transform = value
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
                 len(value) == 9 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'transform' field must be a set or sequence with length 9 and each value of type 'float'"
        self._transform = numpy.array(value, dtype=numpy.float32)

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
    def set_transform(self):
        """Message field 'set_transform'."""
        return self._set_transform

    @set_transform.setter
    def set_transform(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_transform' field must be of type 'bool'"
        self._set_transform = value
