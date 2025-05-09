# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from tracer_msgs/TracerStatus.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg
import tracer_msgs.msg

class TracerStatus(genpy.Message):
  _md5sum = "e0b655d1eae0aa8dc8e69774edae9cbe"
  _type = "tracer_msgs/TracerStatus"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header

int8 MOTOR_ID_FRONT_RIGHT = 0
int8 MOTOR_ID_FRONT_LEFT = 1
int8 MOTOR_ID_REAR_RIGHT = 2
int8 MOTOR_ID_REAR_LEFT = 3

int8 LIGHT_ID_FRONT = 0
int8 LIGHT_ID_REAR = 1

# motion state
float64 linear_velocity
float64 angular_velocity

# base state
uint8 base_state
uint8 control_mode
uint8 fault_code
float64 battery_voltage


# motor state
TracerMotorState[2] motor_states

# light state
bool light_control_enabled
TracerLightState front_light_state

#odometer state
float64 left_odomter
float64 right_odomter

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: tracer_msgs/TracerMotorState
#float64 current
float64 rpm
#float64 temperature

================================================================================
MSG: tracer_msgs/TracerLightState
uint8 mode
uint8 custom_value"""
  # Pseudo-constants
  MOTOR_ID_FRONT_RIGHT = 0
  MOTOR_ID_FRONT_LEFT = 1
  MOTOR_ID_REAR_RIGHT = 2
  MOTOR_ID_REAR_LEFT = 3
  LIGHT_ID_FRONT = 0
  LIGHT_ID_REAR = 1

  __slots__ = ['header','linear_velocity','angular_velocity','base_state','control_mode','fault_code','battery_voltage','motor_states','light_control_enabled','front_light_state','left_odomter','right_odomter']
  _slot_types = ['std_msgs/Header','float64','float64','uint8','uint8','uint8','float64','tracer_msgs/TracerMotorState[2]','bool','tracer_msgs/TracerLightState','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,linear_velocity,angular_velocity,base_state,control_mode,fault_code,battery_voltage,motor_states,light_control_enabled,front_light_state,left_odomter,right_odomter

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TracerStatus, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.linear_velocity is None:
        self.linear_velocity = 0.
      if self.angular_velocity is None:
        self.angular_velocity = 0.
      if self.base_state is None:
        self.base_state = 0
      if self.control_mode is None:
        self.control_mode = 0
      if self.fault_code is None:
        self.fault_code = 0
      if self.battery_voltage is None:
        self.battery_voltage = 0.
      if self.motor_states is None:
        self.motor_states = [tracer_msgs.msg.TracerMotorState() for _ in range(2)]
      if self.light_control_enabled is None:
        self.light_control_enabled = False
      if self.front_light_state is None:
        self.front_light_state = tracer_msgs.msg.TracerLightState()
      if self.left_odomter is None:
        self.left_odomter = 0.
      if self.right_odomter is None:
        self.right_odomter = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.linear_velocity = 0.
      self.angular_velocity = 0.
      self.base_state = 0
      self.control_mode = 0
      self.fault_code = 0
      self.battery_voltage = 0.
      self.motor_states = [tracer_msgs.msg.TracerMotorState() for _ in range(2)]
      self.light_control_enabled = False
      self.front_light_state = tracer_msgs.msg.TracerLightState()
      self.left_odomter = 0.
      self.right_odomter = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2d3Bd().pack(_x.linear_velocity, _x.angular_velocity, _x.base_state, _x.control_mode, _x.fault_code, _x.battery_voltage))
      if len(self.motor_states) != 2:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (2, len(self.motor_states), 'self.motor_states')))
      for val1 in self.motor_states:
        _x = val1.rpm
        buff.write(_get_struct_d().pack(_x))
      _x = self
      buff.write(_get_struct_3B2d().pack(_x.light_control_enabled, _x.front_light_state.mode, _x.front_light_state.custom_value, _x.left_odomter, _x.right_odomter))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.motor_states is None:
        self.motor_states = None
      if self.front_light_state is None:
        self.front_light_state = tracer_msgs.msg.TracerLightState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 27
      (_x.linear_velocity, _x.angular_velocity, _x.base_state, _x.control_mode, _x.fault_code, _x.battery_voltage,) = _get_struct_2d3Bd().unpack(str[start:end])
      self.motor_states = []
      for i in range(0, 2):
        val1 = tracer_msgs.msg.TracerMotorState()
        start = end
        end += 8
        (val1.rpm,) = _get_struct_d().unpack(str[start:end])
        self.motor_states.append(val1)
      _x = self
      start = end
      end += 19
      (_x.light_control_enabled, _x.front_light_state.mode, _x.front_light_state.custom_value, _x.left_odomter, _x.right_odomter,) = _get_struct_3B2d().unpack(str[start:end])
      self.light_control_enabled = bool(self.light_control_enabled)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2d3Bd().pack(_x.linear_velocity, _x.angular_velocity, _x.base_state, _x.control_mode, _x.fault_code, _x.battery_voltage))
      if len(self.motor_states) != 2:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (2, len(self.motor_states), 'self.motor_states')))
      for val1 in self.motor_states:
        _x = val1.rpm
        buff.write(_get_struct_d().pack(_x))
      _x = self
      buff.write(_get_struct_3B2d().pack(_x.light_control_enabled, _x.front_light_state.mode, _x.front_light_state.custom_value, _x.left_odomter, _x.right_odomter))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.motor_states is None:
        self.motor_states = None
      if self.front_light_state is None:
        self.front_light_state = tracer_msgs.msg.TracerLightState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 27
      (_x.linear_velocity, _x.angular_velocity, _x.base_state, _x.control_mode, _x.fault_code, _x.battery_voltage,) = _get_struct_2d3Bd().unpack(str[start:end])
      self.motor_states = []
      for i in range(0, 2):
        val1 = tracer_msgs.msg.TracerMotorState()
        start = end
        end += 8
        (val1.rpm,) = _get_struct_d().unpack(str[start:end])
        self.motor_states.append(val1)
      _x = self
      start = end
      end += 19
      (_x.light_control_enabled, _x.front_light_state.mode, _x.front_light_state.custom_value, _x.left_odomter, _x.right_odomter,) = _get_struct_3B2d().unpack(str[start:end])
      self.light_control_enabled = bool(self.light_control_enabled)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2d3Bd = None
def _get_struct_2d3Bd():
    global _struct_2d3Bd
    if _struct_2d3Bd is None:
        _struct_2d3Bd = struct.Struct("<2d3Bd")
    return _struct_2d3Bd
_struct_3B2d = None
def _get_struct_3B2d():
    global _struct_3B2d
    if _struct_3B2d is None:
        _struct_3B2d = struct.Struct("<3B2d")
    return _struct_3B2d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
