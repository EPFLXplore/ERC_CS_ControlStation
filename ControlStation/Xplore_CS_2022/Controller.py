#
# 27/11/2021
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#
#           ...
#
# @brief: This file contains the Controller (following the Model View Controller
#         design pattern)
#         Here are created all the methods that define the I/O behavior with the
#         user.
#
#================================================================================
import rospy


#================================================================================
'''
'''
class Conrroller:

    def __init__(self, CS_node):
        #the controller is aware of the CS node it is linked to.
        self.application = CS_node

    '''
        Here you should define methods that will be called from javascript. They will
        use the publishers defined in CS_node.py to publish data
    '''
   