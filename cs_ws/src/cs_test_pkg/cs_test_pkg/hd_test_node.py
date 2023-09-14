
import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int32, Int8, Int8MultiArray
from sensor_msgs.msg import JointState, Joy

from avionics_interfaces.msg import Voltage

class HdTestNode(Node):

    def __init__(self):
        super().__init__('hd_test_node')


        #self.publisher_avionics = self.create_publisher(Int32, 'HD/avionics_ToF', 10)
        self.publisher_joint_telemetry = self.create_publisher(JointState, 'ROVER/HD_telemetry', 10)
        self.publiher_artags = self.create_publisher(Int8MultiArray, 'HD/ar_tags', 1)
        self.publisher_voltage = self.create_publisher(Voltage, 'EL/voltage', 1)


        self.subscription_mode = self.create_subscription(Int8,'ROVER/HD_mode',self.mode_callback,10)
        self.subscription_element_id = self.create_subscription(Int8,'ROVER/element_id',self.element_callback,10)
        
       # self.subscription_semiauto_id = self.create_subscription(Int8,'ROVER/element_id',self.id_callback,10)
        self.subscription_maintenance = self.create_subscription(Int8,'ROVER/Maintenance',self.maintenance_callback,10)
        self.subscription_gamepad = self.create_subscription(Joy,'ROVER/HD_gamepad',self.gamepad_callback,10)

        self.subscription_inverse_frame = self.create_subscription(String,'ROVER/HD_inverse_frame' ,self.inverse_frame_callback,10)


        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.j = 0

    def mode_callback(self, msg):
        self.get_logger().info('Received mode: "%d"' % msg.data)

    def element_callback(self, msg):
        self.get_logger().info('Received element: "%d"' % msg.data)

    def goal_callback(self, msg):
        self.get_logger().info('Received goal: "%d"' % msg.data)

    def timer_callback(self):

        msg_joint_telemetry = JointState()
        msg_joint_telemetry.header.stamp = self.get_clock().now().to_msg()
        msg_joint_telemetry.name = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
        msg_joint_telemetry.position = [self.i +0., self.i + 10., self.i + 20., self.i + 30., self.i + 40., self.i + 50.]
        msg_joint_telemetry.velocity = [self.i + 30., self.i + 40., self.i + 50., self.i + 60., self.i + 70., self.i + 80.]
        msg_joint_telemetry.effort = [self.i + 60., self.i + 70., self.i + 80., self.i + 90., self.i + 100., self.i + 110.]
        self.publisher_joint_telemetry.publish(msg_joint_telemetry)

        msg_ar_tags = Int8MultiArray()
        msg_ar_tags.data = [1,1,0,0]
        self.publiher_artags.publish(msg_ar_tags)

        msg_voltage = Voltage()
        msg_voltage.voltage = float(self.i)
        self.publisher_voltage.publish(msg_voltage)

        self.i += 1

    def id_callback(self, msg):
        self.get_logger().info('Received element id: %d' % msg.data)

    def mode_callback(self, msg):
        self.get_logger().info('Received mode: %d' % msg.data)
    
    def maintenance_callback(self, msg):
        self.get_logger().info('Received maintenance: %d' % msg.data)

    def gamepad_callback(self, msg):
        self.j+=1
        if(self.j == 50):
            self.j = 0
            self.get_logger().info('Received gamepad:" %s"' % msg.buttons)
        #self.get_logger().info('Received gamepad:" %s"' % msg.axes)

    def inverse_frame_callback(self, msg):
        self.get_logger().info('Received inverse_frame: "%s"' % msg.data)



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
