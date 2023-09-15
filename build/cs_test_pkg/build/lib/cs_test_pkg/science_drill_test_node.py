
import random
import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int8, Float32MultiArray, Int8MultiArray
from diagnostic_msgs.msg import DiagnosticStatus

from avionics_interfaces.msg import FourInOne, Voltage, NPK, MassArray, SpectroResponse, MassCalibOffset, SpectroRequest

class ScienceTestNode(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        # Log publisher
        self.publisher_log = self.create_publisher(DiagnosticStatus, 'ROVER/CS_log', 10)


        self.publisher_fsm = self.create_publisher(Int8, 'SC/fsm_state_to_cs', 10)
        self.publisher_motors_pos = self.create_publisher(Float32MultiArray, 'SC/motors_pos', 10)
        self.publisher_motors_speed = self.create_publisher(Float32MultiArray, 'SC/motors_speed', 10)
        self.publisher_motors_currents = self.create_publisher(Float32MultiArray, 'SC/motors_currents', 10)
        self.publisher_limit_switches = self.create_publisher(Int8MultiArray, 'SC/limit_switches', 10)

        self.subscription_spectro_request      =        self.create_subscription(SpectroRequest,'El/spectro_req', self.spectro_request,1)
        
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):

        print('Science drill test is running: "%d"' % self.i)

        # msg_log = DiagnosticStatus()
        # msg_log.name = 'Science drill Test'
        # msg_log.level = self.i % 3
        # msg_log.message = 'Diagnostic Status Message from Science drill Test'
        # self.publisher_log.publish(msg_log)

        msg = Int8()
        msg.data = self.i % 22
        self.publisher_fsm.publish(msg)

        msg_0 = Float32MultiArray()
        msg_0.data = [self.i/10, self.i/10+1]
        self.publisher_motors_pos.publish(msg_0)

        msg_1 = Float32MultiArray()
        msg_1.data = [self.i/10+2, self.i/10+3, self.i/10+4]
        self.publisher_motors_speed.publish(msg_1)

        msg_2 = Float32MultiArray()
        msg_2.data = [self.i/10+5, self.i/10+6, self.i/10+7]
        self.publisher_motors_currents.publish(msg_2)

        msg_3 = Int8MultiArray()
        msg_3.data = [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)]
        self.publisher_limit_switches.publish(msg_3)

        self.i += 1


    def spectro_request(self, msg):
        print("spectro_request msg : " + str(msg))

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = ScienceTestNode()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
