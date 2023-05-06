
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from diagnostic_msgs.msg  import DiagnosticStatus


class GamepadTestNode(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        # Log publisher
        self.publisher_log = self.create_publisher(DiagnosticStatus, 'ROVER/CS_log', 10)

        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):

        msg_log = DiagnosticStatus()
        msg_log.name = 'Gamepad Test'
        msg_log.level = self.i % 3
        msg_log.message = 'Diagnostic Status Message from Gamepad Test'
        self.publisher_log.publish(msg_log)


        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = GamepadTestNode()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
