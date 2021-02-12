'''
	@author Emile Hreich

	Model Class (MVC)
'''
import time

class Model:

	'''
	Constructor
	'''
	run_thread = True
	time_array=[0,0,0]
	
		
		

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
			


