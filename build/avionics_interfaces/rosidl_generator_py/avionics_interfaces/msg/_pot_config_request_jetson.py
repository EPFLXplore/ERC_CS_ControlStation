# generated from rosidl_generator_py/resource/_idl.py.em
# with input from avionics_interfaces:msg/PotConfigRequestJetson.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'min_voltages'
# Member 'max_voltages'
# Member 'min_angles'
# Member 'max_angles'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_PotConfigRequestJetson(type):
    """Metaclass of message 'PotConfigRequestJetson'."""

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
                'avionics_interfaces.msg.PotConfigRequestJetson')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__pot_config_request_jetson
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__pot_config_request_jetson
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__pot_config_request_jetson
            cls._TYPE_SUPPORT = module.type_support_msg__msg__pot_config_request_jetson
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__pot_config_request_jetson

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class PotConfigRequestJetson(metaclass=Metaclass_PotConfigRequestJetson):
    """Message class 'PotConfigRequestJetson'."""

    __slots__ = [
        '_destination_id',
        '_min_voltages',
        '_max_voltages',
        '_min_angles',
        '_max_angles',
        '_enabled_channels',
        '_remote_command',
        '_set_min_voltages',
        '_set_max_voltages',
        '_set_min_angles',
        '_set_max_angles',
        '_set_channels_status',
    ]

    _fields_and_field_types = {
        'destination_id': 'uint16',
        'min_voltages': 'float[4]',
        'max_voltages': 'float[4]',
        'min_angles': 'float[4]',
        'max_angles': 'float[4]',
        'enabled_channels': 'boolean[4]',
        'remote_command': 'boolean',
        'set_min_voltages': 'boolean',
        'set_max_voltages': 'boolean',
        'set_min_angles': 'boolean',
        'set_max_angles': 'boolean',
        'set_channels_status': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 4),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 4),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 4),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 4),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('boolean'), 4),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
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
        if 'min_voltages' not in kwargs:
            self.min_voltages = numpy.zeros(4, dtype=numpy.float32)
        else:
            self.min_voltages = numpy.array(kwargs.get('min_voltages'), dtype=numpy.float32)
            assert self.min_voltages.shape == (4, )
        if 'max_voltages' not in kwargs:
            self.max_voltages = numpy.zeros(4, dtype=numpy.float32)
        else:
            self.max_voltages = numpy.array(kwargs.get('max_voltages'), dtype=numpy.float32)
            assert self.max_voltages.shape == (4, )
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
        self.enabled_channels = kwargs.get(
            'enabled_channels',
            [bool() for x in range(4)]
        )
        self.remote_command = kwargs.get('remote_command', bool())
        self.set_min_voltages = kwargs.get('set_min_voltages', bool())
        self.set_max_voltages = kwargs.get('set_max_voltages', bool())
        self.set_min_angles = kwargs.get('set_min_angles', bool())
        self.set_max_angles = kwargs.get('set_max_angles', bool())
        self.set_channels_status = kwargs.get('set_channels_status', bool())

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
        if all(self.min_voltages != other.min_voltages):
            return False
        if all(self.max_voltages != other.max_voltages):
            return False
        if all(self.min_angles != other.min_angles):
            return False
        if all(self.max_angles != other.max_angles):
            return False
        if self.enabled_channels != other.enabled_channels:
            return False
        if self.remote_command != other.remote_command:
            return False
        if self.set_min_voltages != other.set_min_voltages:
            return False
        if self.set_max_voltages != other.set_max_voltages:
            return False
        if self.set_min_angles != other.set_min_angles:
            return False
        if self.set_max_angles != other.set_max_angles:
            return False
        if self.set_channels_status != other.set_channels_status:
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
    def min_voltages(self):
        """Message field 'min_voltages'."""
        return self._min_voltages

    @min_voltages.setter
    def min_voltages(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'min_voltages' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 4, \
                "The 'min_voltages' numpy.ndarray() must have a size of 4"
            self._min_voltages = value
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
                "The 'min_voltages' field must be a set or sequence with length 4 and each value of type 'float'"
        self._min_voltages = numpy.array(value, dtype=numpy.float32)

    @property
    def max_voltages(self):
        """Message field 'max_voltages'."""
        return self._max_voltages

    @max_voltages.setter
    def max_voltages(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'max_voltages' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 4, \
                "The 'max_voltages' numpy.ndarray() must have a size of 4"
            self._max_voltages = value
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
                "The 'max_voltages' field must be a set or sequence with length 4 and each value of type 'float'"
        self._max_voltages = numpy.array(value, dtype=numpy.float32)

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
    def enabled_channels(self):
        """Message field 'enabled_channels'."""
        return self._enabled_channels

    @enabled_channels.setter
    def enabled_channels(self, value):
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
                 all(isinstance(v, bool) for v in value) and
                 True), \
                "The 'enabled_channels' field must be a set or sequence with length 4 and each value of type 'bool'"
        self._enabled_channels = value

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
    def set_min_voltages(self):
        """Message field 'set_min_voltages'."""
        return self._set_min_voltages

    @set_min_voltages.setter
    def set_min_voltages(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_min_voltages' field must be of type 'bool'"
        self._set_min_voltages = value

    @property
    def set_max_voltages(self):
        """Message field 'set_max_voltages'."""
        return self._set_max_voltages

    @set_max_voltages.setter
    def set_max_voltages(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_max_voltages' field must be of type 'bool'"
        self._set_max_voltages = value

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

    @property
    def set_channels_status(self):
        """Message field 'set_channels_status'."""
        return self._set_channels_status

    @set_channels_status.setter
    def set_channels_status(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_channels_status' field must be of type 'bool'"
        self._set_channels_status = value
