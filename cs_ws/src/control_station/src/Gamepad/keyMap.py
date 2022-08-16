from enum import Enum

class Keymap(Enum):
    BTN_CROSS = 304
    BTN_CIRCLE = 305
    BTN_TRIANGLE = 307
    BTN_SQUARE = 308

    BTN_L1 = 310
    BTN_R1 = 311
    BTN_L2 = 312
    BTN_R2 = 313
    BTN_LT = 317  # L3
    BTN_RT = 318  # R3

    BTN_SHARE = 314
    BTN_OPTIONS = 315
    BTN_PS = 316

    AXE_LX = 0  
    AXE_LY = 1
    AXE_RX = 3
    AXE_RY = 4

    AXE_L2 = 2
    AXE_R2 = 5

    AXE_DX = 16
    AXE_DY = 17