from enum import IntEnum
from tkinter.messagebox import RETRY
#=====================================================
#FINITE STATE MACHINE

class Task(IntEnum):
    IDLE        = 0
    MANUAL      = 1
    NAVIGATION  = 2
    MAINTENANCE = 3
    SCIENCE     = 4
    
  
class Instruction(IntEnum):
  LAUNCH = 1
  ABORT  = 2
  WAIT   = 3
  RESUME = 4
  RETRY  = 5

# ROVER_STATE    = task.IDLE
# INSTRUCTION    = instruction.WORK
# TASK_COMPLETED = False
# CONFIRMATION   = 0
#=====================================================