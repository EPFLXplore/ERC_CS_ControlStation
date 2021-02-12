'''
	@author Emile Hreich

	Model Class (MVC)
'''
import rospy
from std_msgs.msg import String, Float32, Float32MultiArray

class Model:

	'''
	Constructor
	'''

	def __init__(self):

		a=0
	
	def callback_barotemp(msg):
		print("Pressure: " + str(msg.data[0]), "\n", \
					"Temperature: ", msg.data[1])
		# rospy.loginfo("Pressure: " + str(msg.data[0]), "\n", \
		#               "Temperature: ", msg.data[1])

	def callback_accelmag(msg):
		print("acceleration: ", msg.data[0:3], "\n", \
					"angular: ", msg.data[3:6], "\n", \
					"magneto: ", msg.data[6:], "\n")

	def callback_gripper(msg):
		print("Gripper voltage: ", msg.data, "\n")

	def callback_system(msg):
		print("Battery: ", msg.data[0], "\n", \
					"State: ", msg.data[1])

	def callback_voltages(msg):
		print("voltages: ", msg.data[0], "\n")

	def callback_currents(msg):
		print("currents: ", msg.data[0], "\n")

	def callback_measures(msg):
		print("Mass: ", msg.data, "\n")

	
