# generated from rosidl_generator_py/resource/_idl.py.em
# with input from avionics_interfaces:msg/MassConfigRequestJetson.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'offset'
# Member 'scale'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MassConfigRequestJetson(type):
    """Metaclass of message 'MassConfigRequestJetson'."""

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
                'avionics_interfaces.msg.MassConfigRequestJetson')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__mass_config_request_jetson
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__mass_config_request_jetson
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__mass_config_request_jetson
            cls._TYPE_SUPPORT = module.type_support_msg__msg__mass_config_request_jetson
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__mass_config_request_jetson

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MassConfigRequestJetson(metaclass=Metaclass_MassConfigRequestJetson):
    """Message class 'MassConfigRequestJetson'."""

    __slots__ = [
        '_destination_id',
        '_offset',
        '_scale',
        '_alpha',
        '_enabled_channels',
        '_remote_command',
        '_set_offset',
        '_set_scale',
        '_set_alpha',
        '_set_channels_status',
    ]

    _fields_and_field_types = {
        'destination_id': 'uint16',
        'offset': 'float[4]',
        'scale': 'float[4]',
        'alpha': 'float',
        'enabled_channels': 'boolean[4]',
        'remote_command': 'boolean',
        'set_offset': 'boolean',
        'set_scale': 'boolean',
        'set_alpha': 'boolean',
        'set_channels_status': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 4),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 4),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('boolean'), 4),  # noqa: E501
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
        if 'offset' not in kwargs:
            self.offset = numpy.zeros(4, dtype=numpy.float32)
        else:
            self.offset = numpy.array(kwargs.get('offset'), dtype=numpy.float32)
            assert self.offset.shape == (4, )
        if 'scale' not in kwargs:
            self.scale = numpy.zeros(4, dtype=numpy.float32)
        else:
            self.scale = numpy.array(kwargs.get('scale'), dtype=numpy.float32)
            assert self.scale.shape == (4, )
        self.alpha = kwargs.get('alpha', float())
        self.enabled_channels = kwargs.get(
            'enabled_channels',
            [bool() for x in range(4)]
        )
        self.remote_command = kwargs.get('remote_command', bool())
        self.set_offset = kwargs.get('set_offset', bool())
        self.set_scale = kwargs.get('set_scale', bool())
        self.set_alpha = kwargs.get('set_alpha', bool())
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
        if all(self.offset != other.offset):
            return False
        if all(self.scale != other.scale):
            return False
        if self.alpha != other.alpha:
            return False
        if self.enabled_channels != other.enabled_channels:
            return False
        if self.remote_command != other.remote_command:
            return False
        if self.set_offset != other.set_offset:
            return False
        if self.set_scale != other.set_scale:
            return False
        if self.set_alpha != other.set_alpha:
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
    def offset(self):
        """Message field 'offset'."""
        return self._offset

    @offset.setter
    def offset(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'offset' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 4, \
                "The 'offset' numpy.ndarray() must have a size of 4"
            self._offset = value
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
                "The 'offset' field must be a set or sequence with length 4 and each value of type 'float'"
        self._offset = numpy.array(value, dtype=numpy.float32)

    @property
    def scale(self):
        """Message field 'scale'."""
        return self._scale

    @scale.setter
    def scale(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'scale' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 4, \
                "The 'scale' numpy.ndarray() must have a size of 4"
            self._scale = value
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
                "The 'scale' field must be a set or sequence with length 4 and each value of type 'float'"
        self._scale = numpy.array(value, dtype=numpy.float32)

    @property
    def alpha(self):
        """Message field 'alpha'."""
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'alpha' field must be of type 'float'"
        self._alpha = value

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
    def set_offset(self):
        """Message field 'set_offset'."""
        return self._set_offset

    @set_offset.setter
    def set_offset(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_offset' field must be of type 'bool'"
        self._set_offset = value

    @property
    def set_scale(self):
        """Message field 'set_scale'."""
        return self._set_scale

    @set_scale.setter
    def set_scale(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_scale' field must be of type 'bool'"
        self._set_scale = value

    @property
    def set_alpha(self):
        """Message field 'set_alpha'."""
        return self._set_alpha

    @set_alpha.setter
    def set_alpha(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'set_alpha' field must be of type 'bool'"
        self._set_alpha = value

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
