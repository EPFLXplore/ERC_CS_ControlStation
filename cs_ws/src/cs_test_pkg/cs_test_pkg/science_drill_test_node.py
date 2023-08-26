
import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int8, Float32MultiArray
from diagnostic_msgs.msg import DiagnosticStatus


class ScienceTestNode(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        # Log publisher
        self.publisher_log = self.create_publisher(DiagnosticStatus, 'ROVER/CS_log', 10)


        self.publisher_fsm = self.create_publisher(Int8, 'SC/fsm_state_to_cs', 10)
        self.publisher_motors_pos = self.create_publisher(Float32MultiArray, 'SC/motors_pos', 10)
        self.publisher_motors_speed = self.create_publisher(Float32MultiArray, 'SC/motors_speed', 10)
        self.publisher_motors_currents = self.create_publisher(Float32MultiArray, 'SC/motors_currents', 10)
        self.publisher_limit_switches = self.create_publisher(Float32MultiArray, 'SC/limit_switches', 10)

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

        msg = String()
        msg.data = 'Hello World: %d' % self.i
        #self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


        msg = "IDLE" + str(self.i)
        self.publisher_sc_fsm_state.publish(msg)


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
