
import rclpy
from rclpy.node import Node

from std_msgs.msg         import Int8MultiArray, Int8, Int32, Int32MultiArray, Bool, String, Int16MultiArray, Int16, Float32MultiArray
from diagnostic_msgs.msg  import DiagnosticStatus

class ElecTestNode(Node):

    def __init__(self):
        super().__init__('elec_test_publisher')

        # Log publisher
        self.publisher_log = self.create_publisher(DiagnosticStatus, 'ROVER/CS_log', 10)

        self.publisher_mass             = self.create_publisher(Float32MultiArray, 'EL/mass', 10)
        self.publisher_spectrometer     = self.create_publisher(Float32MultiArray, 'EL/spectrometer', 10)
        self.publisher_npk              = self.create_publisher(Float32MultiArray, 'EL/npk', 10)
        self.publisher_potentiometers   = self.create_publisher(Float32MultiArray, 'EL/potentiometers', 10)
        self.publisher_LED_confirm      = self.create_publisher(Float32MultiArray, 'EL/LED_confirm', 10)
        self.publisher_HD_voltmeter     = self.create_publisher(Int8,              'EL/HD_voltmeter', 10)
        self.publisher_HD_laser         = self.create_publisher(Bool,              'EL/HD_laser', 10)
        self.publisher_four_in_one      = self.create_publisher(Float32MultiArray, 'EL/four_in_one', 10)


        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):

        msg_log = DiagnosticStatus()
        msg_log.name = 'Elec Test'
        #msg_log.level = self.i % 3
        msg_log.message = 'Diagnostic Status Message from Elec Test'
        self.publisher_log.publish(msg_log)

        msg_float_32_multi = Float32MultiArray()
        msg_float_32_multi.data = [float(self.i), float(self.i + 10)]

        msg_int_8 = Int8()
        msg_int_8.data = self.i

        msg_bool = Bool()
        msg_bool.data = self.i % 2 == 0

        # self.publisher_mass.publish(msg_float_32_multi)
        # self.publisher_spectrometer.publish(msg_float_32_multi)
        # self.publisher_npk.publish(msg_float_32_multi)
        # self.publisher_potentiometers.publish(msg_float_32_multi)
        # self.publisher_LED_confirm.publish(msg_float_32_multi)
        # self.publisher_HD_voltmeter.publish(msg_int_8)
        # self.publisher_HD_laser.publish(msg_bool)
        self.publisher_four_in_one.publish(msg_float_32_multi)

        print(msg_float_32_multi.data)
        
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = ElecTestNode()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
