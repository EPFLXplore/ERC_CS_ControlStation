
import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int32, Int8
from sensor_msgs.msg import JointState


class HdTestNode(Node):

    def __init__(self):
        super().__init__('minimal_publisher')


        self.publisher_avionics = self.create_publisher(Int32, 'HD/avionics_ToF', 10)
        self.publisher_joint_telemetry = self.create_publisher(JointState, 'HD/arm_control/joint_telemetry', 10)

        self.subscription_semiauto_id = self.create_subscription(Int8,'ROVER/HD_SemiAuto_Id',self.goal_callback,10)
        self.subscription_mode = self.create_subscription(Int8,'ROVER/HD_mode',self.goal_callback,10)
        self.subscription_maintenance = self.create_subscription(Int8,'ROVER/Maintenance',self.goal_callback,10)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):

        msg_avionics = Int32()
        msg_avionics.data = self.i
        self.publisher_avionics.publish(msg_avionics)

        msg_joint_telemetry = JointState()
        msg_joint_telemetry.header.stamp = self.get_clock().now().to_msg()
        msg_joint_telemetry.name = ['joint1', 'joint2', 'joint3']
        msg_joint_telemetry.position = [self.i, self.i + 10, self.i + 20]
        msg_joint_telemetry.velocity = [self.i + 30, self.i + 40, self.i + 50]
        msg_joint_telemetry.effort = [self.i + 60, self.i + 70, self.i + 80]
        self.publisher_joint_telemetry.publish(msg_joint_telemetry)

        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = HdTestNode()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
