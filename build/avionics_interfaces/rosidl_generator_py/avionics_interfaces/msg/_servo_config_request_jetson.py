# generated from rosidl_generator_py/resource/_idl.py.em
# with input from avionics_interfaces:msg/ServoConfigRequestJetson.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'min_duty'
# Member 'max_duty'
# Member 'min_angles'
# Member 'max_angles'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ServoConfigRequestJetson(type):
    """Metaclass of message 'ServoConfigRequestJetson'."""

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
                'avionics_interfaces.msg.ServoConfigRequestJetson')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__servo_config_request_jetson
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__servo_config_request_jetson
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__servo_config_request_jetson
            cls._TYPE_SUPPORT = module.type_support_msg__msg__servo_config_request_jetson
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__servo_config_request_jetson

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ServoConfigRequestJetson(metaclass=Metaclass_ServoConfigRequestJetson):
    """Message class 'ServoConfigRequestJetson'."""

    __slots__ = [
        '_destination_id',
        '_min_duty',
        '_max_duty',
        '_min_angles',
        '_max_angles',
        '_remote_command',
        '_set_min_duty',
        '_set_max_duty',
        '_set_min_angles',
        '_set_max_angles',
    ]

    _fields_and_field_types = {
        'destination_id': 'uint16',
        'min_duty': 'float[4]',
        'max_duty': 'float[4]',
        'min_angles': 'float[4]',
        'max_angles': 'float[4]',
        'remote_command': 'boolean',
        'set_min_duty': 'boolean',
        'set_max_duty': 'boolean',
        'set_min_angles': 'boolean',
        'set_max_angles': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 4),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 4),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 4),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 4),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.destination_id = kwargs.get('destination_id', int())
        if 'min_duty' not in kwargs:
            self.min_duty = numpy.zeros(4, dtype=numpy.float32)
        else:
            self.min_duty = numpy.array(kwargs.get('min_duty'), dtype=numpy.float32)
            assert self.min_duty.shape == (4, )
        if 'max_duty' not in kwargs:
            self.max_duty = numpy.zeros(4, dtype=numpy.float32)
        else:
            self.max_duty = numpy.array(kwargs.get('max_duty'), dtype=numpy.float32)
            assert self.max_duty.shape == (4, )
        if 'min_angles' not in kwargs:
            self.min_angles = numpy.zeros(4, dtype=numpy.float32)
        else:
            self.min_angles = numpy.array(kwargs.get('min_angles'), dtype=numpy.float32)
            assert self.min_angles.shape == (4, )
        if 'max_angles' not in kwargs:
            self.max_angles = numpy.zeros(4, dtype=numpy.float32)
        else:
            self.max_angles = numpy.array(kwargs.get('max_angles'), dtype=numpy.float32)
            assert self.max_angles.shape == (4, )
        self.remote_command = kwargs.get('remote_command', bool())
        self.set_min_duty = kwargs.get('set_min_duty', bool())
        self.set_max_duty = kwargs.get('set_max_duty', bool())
        self.set_min_angles = kwargs.get('set_min_angles', bool())
        self.set_max_angles = kwargs.get('set_max_angles', bool())

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
        if all(self.min_duty != other.min_duty):
            return False
        if all(self.max_duty != other.max_duty):
            return False
        if all(self.min_angles != other.min_angles):
            return False
        if all(self.max_angles != other.max_angles):
            return False
        if self.remote_command != other.remote_command:
            return False
        if self.set_min_duty != other.set_min_duty:
            return False
        if self.set_max_duty != other.set_max_duty:
            return False
        if self.set_min_angles != other.set_min_angles:
            return False
        if self.set_max_angles != other.set_max_angles:
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
    def min_duty(self):
        """Message field 'min_duty'."""
        return self._min_duty

    @min_duty.setter
    def min_duty(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'min_duty' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 4, \
                "The 'min_duty' numpy.ndarray() must have a size of 4"
            self._min_duty = value
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
                 len(value) == 4 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'min_duty' field must be a set or sequence with length 4 and each value of type 'float'"
        self._min_duty = numpy.array(value, dtype=numpy.float32)

    @property
    def max_duty(self):
        """Message field 'max_duty'."""
        return self._max_duty

    @max_duty.setter
    def max_duty(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'max_duty' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 4, \
                "The 'max_duty' numpy.ndarray() must have a size of 4"
            self._max_duty = value
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
                 len(value) == 4 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'max_duty' field must be a set or sequence with length 4 and each value of type 'float'"
        self._max_duty = numpy.array(value, dtype=numpy.float32)

    @property
    def min_angles(self):
        """Message field 'min_angles'."""
        return self._min_angles

    @min_angles.setter
    def min_angles(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'min_angles' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 4, \
                "The 'min_angles' numpy.ndarray() must have a size of 4"
            self._min_angles = value
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
                 len(value) == 4 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'min_angles' field must be a set or sequence with length 4 and each value of type 'float'"
        self._min_angles = numpy.array(value, dtype=numpy.float32)

    @property
    def max_angles(self):
        """Message field 'max_angles'."""
        return self._max_angles

    @max_angles.setter
    def max_angles(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'max_angles' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 4, \
                "The 'max_angles' numpy.ndarray() must have a size of 4"
            self._max_angles = value
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
                 len(value) == 4 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'max_angles' field must be a set or sequence with length 4 and each value of type 'float'"
        self._max_angles = numpy.array(value, dtype=numpy.float32)

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
    def set_min_duty(self):
        """Message field 'set_min_duty'."""
        return self._set_min_duty

    @set_min_duty.setter
    def set_min_duty(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_min_duty' field must be of type 'bool'"
        self._set_min_duty = value

    @property
    def set_max_duty(self):
        """Message field 'set_max_duty'."""
        return self._set_max_duty

    @set_max_duty.setter
    def set_max_duty(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_max_duty' field must be of type 'bool'"
        self._set_max_duty = value

    @property
    def set_min_angles(self):
        """Message field 'set_min_angles'."""
        return self._set_min_angles

    @set_min_angles.setter
    def set_min_angles(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_min_angles' field must be of type 'bool'"
        self._set_min_angles = value

    @property
    def set_max_angles(self):
        """Message field 'set_max_angles'."""
        return self._set_max_angles

    @set_max_angles.setter
    def set_max_angles(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_max_angles' field must be of type 'bool'"
        self._set_max_angles = value
