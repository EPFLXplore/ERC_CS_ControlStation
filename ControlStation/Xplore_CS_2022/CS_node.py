#
# 27/11/2021
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#
#           ...
#
# @brief: This file contains the Application class of the backend. It will
#         create the ROS node for the Control Station and take care of creating
#         and subscribing to the needed ROS topic. It will also define and run 
#         the listening thread that will receive the data from the rover and store
#         it into the database.
#
#================================================================================
from threading import Thread
import rospy
import Controller



#================================================================================
'''
    This class creates a listening thread, initializes all ROS publishers and subscribes
    to all the needed topics
'''
class Application(Thread):

    def __init__(self, threadID, name):

        Thread.__init__(self)
        self.threadID = threadID
        self.name     = name
        
        self.controller = Controller(self)
        rospy.init_node('CONTROL_STATION', anonymous=True)

        '''
        Define the ROS topics: subscriptions and publishers
        '''
        
        

    def run(self):
        print("Listening")
        rospy.spin() 

#================================================================================
'''
    Here you should create all the ROS callback functions that will receive the data
    and store it into the data base using django commands
'''


#================================================================================
#MAIN
if __name__ == '__main__':

  
  
  # Create The reception thread
  listener  = Application(1, "Reception loop")
  # Start the reception thread
  listener.start()


  
