from curses.ascii import US
from enum import IntEnum
from tkinter import image_names
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

class Science(IntEnum):
  LOAD_HIST = 1
  ABORT = 2
  MASS_MEASUREMENT = 3
  # ... = 4 ?
  RETRY = 5
  CONFIRM = 6
  CALIBRATION_MASS = 7
  EXIT = 8
  TAKE_PIC = 9

  START_SAMPLING_0 = 10
  START_SAMPLING_1 = 11
  START_SAMPLING_2 = 12

  USER_CONFIRM_0 = 20
  USER_CONFIRM_1 = 21
  USER_CONFIRM_2 = 22

  IMG_ANALYSIS_0 = 30
  IMG_ANALYSIS_1 = 31
  IMG_ANALYSIS_2 = 32

  HUMIDITY_MEASUREMENT_0 = 40
  HUMIDITY_MEASUREMENT_1 = 41
  HUMIDITY_MEASUREMENT_2 = 42

# ROVER_STATE    = task.IDLE
# INSTRUCTION    = instruction.WORK
# TASK_COMPLETED = False
# CONFIRMATION   = 0
#=====================================================