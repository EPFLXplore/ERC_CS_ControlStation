from enum import IntEnum

#=====================================================
#FINITE STATE MACHINE

class Task(IntEnum):
    IDLE        = 0
    MANUAL      = 1
    NAVIGATION  = 2
    MAINTENANCE = 3
    SCIENCE     = 4
    DRONE       = 5
    WAITING     = 6
    
  
class Instruction(IntEnum):
  LAUNCH  = 1
  ABORT   = 2
  WAIT    = 3
  RESUME  = 4
  RETRY   = 5
  LATCH   = 6
  OKDRONE = 7
  


# ROVER_STATE    = task.IDLE
# INSTRUCTION    = instruction.WORK
# TASK_COMPLETED = False
# CONFIRMATION   = 0
#=====================================================
