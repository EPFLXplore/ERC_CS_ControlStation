
from enum import IntEnum

class TabList(IntEnum):
	MENU           = 0
	NAV_MANUAL     = 1
	NAV_SEMIAUTO   = 2
	NAV_AUTO       = 3
	HD_MANUAL      = 4
	HD_AUTO        = 5
	SC_DATA        = 6
	SC_DRILL       = 7
	CAMERAS        = 8
	LOGS           = 9



class Tabs():
	
	nav_manual_access       = [1,0,0,0,1,1,1,0,1,1]
	nav_semi_auto_access    = [1,0,0,0,1,1,1,0,1,1]
	nav_semi_access         = [1,0,0,0,1,1,1,0,1,1]
	hd_manual_access        = [1,1,1,1,0,0,1,0,1,1]
	hd_auto_access          = [1,1,1,1,0,0,1,0,1,1]
	sc_data_access          = [1,1,1,1,1,1,1,1,1,1]
	sc_drill_access         = [1,0,0,0,0,0,1,0,1,1]
	cameras_access          = [1,1,1,1,1,1,1,1,1,1]
	logs_access             = [1,1,1,1,1,1,1,1,1,1]

	def __init__(self):
		self.usersState = []
		
	def availableTabs(self):
	    available = [1,1,1,1,1,1,1,1,1,1]
	    
        
        
