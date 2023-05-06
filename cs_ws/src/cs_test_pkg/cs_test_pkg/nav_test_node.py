
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from diagnostic_msgs.msg import DiagnosticStatus

from std_msgs.msg import Int8MultiArray, Int8, Int32, Int32MultiArray, Bool, String, Int16MultiArray, Int16, Float32MultiArray


class NavTestNode(Node):

    def __init__(self):
        super().__init__('nav_test_publisher')
        
        # Log publisher
        self.publisher_log = self.create_publisher(DiagnosticStatus, 'ROVER/CS_log', 10)

        self.publisher_odometry = self.create_publisher(Odometry, 'NAV/odometry/filtered', 10)
        
        #TODO
        #self.subscription_move_base = self.create_subscription(String,'ROVER/move_base/cancel',self.listener_callback,10)
        self.subscription_goal =        self.create_subscription(PoseStamped,'ROVER/NAV_goal',self.goal_callback,10)
        self.subscription_navigation =  self.create_subscription(Int8,'ROVER/Navigation',self.navigation_callback,10)


        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg_log = DiagnosticStatus()
       
        msg_log.name = 'Nav Test'
        msg_log.level = (self.i % 3). to_bytes(1,"big")
        msg_log.message = 'Diagnostic Status Message from Nav Test'
        self.publisher_log.publish(msg_log)
        print("Messaage send ")

        msg = Odometry()
        msg.pose.pose.position.x = float(self.i)
        msg.pose.pose.position.y = float(self.i + 10)
        msg.pose.pose.position.z = float(self.i + 20)
        msg.pose.pose.orientation.x = float(self.i + 30)
        msg.pose.pose.orientation.y = float(self.i + 40)
        msg.pose.pose.orientation.z = float(self.i + 50)
        msg.child_frame_id = "nav test child frame id"
        msg.header.frame_id = "nav test header"
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.twist.twist.linear.x = float(self.i + 60)
        msg.twist.twist.linear.y = float(self.i + 70)
        msg.twist.twist.linear.z = float(self.i + 80)
        msg.twist.twist.angular.x = float(self.i + 90)
        msg.twist.twist.angular.y = float(self.i + 100)
        msg.twist.twist.angular.z = float(self.i + 110)

        self.publisher_odometry.publish(msg)
        self.i += 1


    def goal_callback(self, msg):
        self.get_logger().info('Goal callback: "%s"' % msg.data)

    def navigation_callback(self, msg):
        self.get_logger().info('Navigation callback: "%s"' % msg.data)



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = NavTestNode()

    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
