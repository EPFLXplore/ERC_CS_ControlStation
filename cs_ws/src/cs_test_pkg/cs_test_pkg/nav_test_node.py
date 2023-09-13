
import math
import random
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped, Point, Pose
from diagnostic_msgs.msg import DiagnosticStatus

from std_msgs.msg import Int8MultiArray, Int8, Int32, Int32MultiArray, Bool, String, Int16MultiArray, Int16, Float32MultiArray
from avionics_interfaces.msg import AngleArray

from transforms3d.euler import euler2quat
from diagnostic_msgs.msg  import DiagnosticStatus

from custom_msg.msg import Wheelstatus, Motorcmds

class NavTestNode(Node):

    def __init__(self):
        super().__init__('nav_test_publisher')
        
        # Log publisher
        self.publisher_log = self.create_publisher(DiagnosticStatus, 'ROVER/CS_log', 10)
        self.publisher_odometry = self.create_publisher(Odometry, '/lio_sam/odom', 10)
        self.publisher_path = self.create_publisher(Path, '/path', 1)
        self.publisher_wheel_ang = self.create_publisher(Wheelstatus, 'NAV/absolute_encoders', 10)
        self.publisher_motorcmds = self.create_publisher(Motorcmds, 'NAV/displacement', 10)
        
        #TODO
        #self.subscription_move_base = self.create_subscription(String,'ROVER/move_base/cancel',self.listener_callback,10)
        self.subscription_goal =        self.create_subscription(PoseStamped,'ROVER/NAV_goal',self.goal_callback,10)
        self.subscription_navigation =  self.create_subscription(String,'ROVER/NAV_status',self.navigation_callback,10)
        self.subscription_mode =       self.create_subscription(String,'ROVER/NAV_mode',self.mode_callback,10)
        self.subscription_kinematic = self.create_subscription(String,'ROVER/NAV_kinematic',self.kinematic_callback,10)
        self.subscription_starting_point = self.create_subscription(PoseStamped,'/lio_sam/initial_pose',self.starting_point_callback,10)

        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        print('Nav test is running...')

    def timer_callback(self):



        # msg_log = DiagnosticStatus()
        # msg_log.name = 'Nav Test'
        # msg_log.level = (self.i % 3). to_bytes(1,"big")
        # msg_log.message = 'Diagnostic Status Message from Nav Test'
        # self.publisher_log.publish(msg_log)

        msg = Odometry()
        msg.pose.pose.position.x = random.uniform(-10, 10)
        msg.pose.pose.position.y = random.uniform(0, 25)
        msg.pose.pose.position.z = msg.pose.pose.position.z + random.uniform(-3, 3)

        euler = [random.uniform(0, 360) * math.pi / 180, random.uniform(0, 360) * math.pi / 180, random.uniform(0, 360) * math.pi / 180]
        angle = euler2quat(euler[0], euler[1], euler[2])
        msg.pose.pose.orientation.w = angle[0]
        msg.pose.pose.orientation.x = angle[1]
        msg.pose.pose.orientation.y = angle[2]
        msg.pose.pose.orientation.z = angle[3]

        msg.child_frame_id = "nav test child frame id"
        msg.header.frame_id = "nav test header"
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.twist.twist.linear.x = float(self.i/10 + 60)
        msg.twist.twist.linear.y = float(self.i/10 + 70)
        msg.twist.twist.linear.z = float(self.i/10 + 80)
        msg.twist.twist.angular.x = float(self.i/10 + 90)
        msg.twist.twist.angular.y = float(self.i/10 + 100)
        msg.twist.twist.angular.z = float(self.i/10 + 110)

        path = Path()
        #path.poses = [PoseStamped(pose = Pose(point= Point(1.,3. ,2. )))]
        self.publisher_path.publish(path)

        motor = Motorcmds()
        motor.modedeplacement = "wallah"
        motor.info = "yasmin"
        self.publisher_motorcmds.publish(motor)

        status = Wheelstatus()
        status.data = [1., 2., 3., 4., 5., 6., 7., 8.]
        status.state = [False, False, True, True, False, False, True, True]
        self.publisher_wheel_ang.publish(status)
       

        self.publisher_odometry.publish(msg)
        self.i += 1

    def goal_callback(self, msg):
        self.get_logger().info('Goal callback :' + str(msg.pose.position.x) + " " + str(msg.pose.position.y) + " " + str(msg.pose.position.z))

    def navigation_callback(self, msg):
        self.get_logger().info('Navigation callback: "%s"' % msg.data)

    def mode_callback(self, msg):
        self.get_logger().info('Mode callback: "%s"' % msg.data)

    def kinematic_callback(self, msg):
        self.get_logger().info('Kinematic callback: "%s"' % msg.data)

    def starting_point_callback(self, msg):
        self.get_logger().info('Starting point callback :' + str(msg.pose.position.x) + " " + str(msg.pose.position.y) + " " + str(msg.pose.position.z))


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = NavTestNode()

    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
