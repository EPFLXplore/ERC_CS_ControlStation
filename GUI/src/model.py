'''
	@author Emile Hreich

	Model Class (MVC)
'''
import time

class Model:


	run_thread = True
	time_array=[0,0,0]

	#AVIONICS DATA
	barotemp = [-1,-1]
	accelmag = [-1, -1, -1]
	gripper = 0.0
	system = []
	voltages = [-1,-1,-1,-1]
	currents = [-1, -1, -1, -1]
	measures = 0.0

	#NAVIGATION DATA
	waypoint = [-1, -1, -1]
	tags = []
	signal_AM = False
	rover_state = 0
	nav_logs = ""
	mission_state_d1 = 0
	#current position
	
	#SCIENCE DATA

	#HANDLING DEVICE DATA
	
		
	def get_time(self):
		s=0
		m=0
		h=0
		while s<=60:

			
			time.sleep(1)
			s+=1
			if s==60:
				m+=1
				s=0
				if (m == 60):
					h += 1
					m = 0
			Model.time_array[0] = h
			Model.time_array[1] = m
			Model.time_array[2] = s
			if (Model.run_thread == False):
				break
			


