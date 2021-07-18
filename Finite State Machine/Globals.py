from enum import IntEnum
#=====================================================
#FINITE STATE MACHINE

class task(IntEnum):
  IDLE        = 1
  MAINTENANCE = 2
  SCIENCE     = 3
  PROBING     = 4
  NAVIGATION  = 5
  MANUAL      = 6
  WAITING     = 7

class instruction(IntEnum):
  WORK   = 1
  WAIT   = 2
  STOP   = 3
  RESUME = 4

# ROVER_STATE    = task.IDLE
# INSTRUCTION    = instruction.WORK
# TASK_COMPLETED = False
# CONFIRMATION   = 0
#=====================================================