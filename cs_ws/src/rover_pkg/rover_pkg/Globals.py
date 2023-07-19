#from curses.ascii import US
#from distutils.log import INFO
from enum import IntEnum
#from tkinter import image_names
#from tkinter.messagebox import RETRY
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


class ScienceTask(IntEnum):
  ABORT    = 0
  RETRY    = 1
  CONFIRM  = 2
  HUMIDITY = 3
  PARAMS   = 4
  INFO     = 5
  STATE    = 6
  TAKE_PIC = 9

  START_SAMPLING_0 = 10
  START_SAMPLING_1 = 11
  START_SAMPLING_2 = 12

  ROT_TO_PIC_0   = 20
  ROT_TO_PIC_1   = 21
  ROT_TO_PIC_2   = 22

  MASS_MEASURE_0 = 30
  MASS_MEASURE_1 = 31
  MASS_MEASURE_2 = 32

  


# ROVER_STATE    = task.IDLE
# INSTRUCTION    = instruction.WORK
# TASK_COMPLETED = False
# CONFIRMATION   = 0
#=====================================================
