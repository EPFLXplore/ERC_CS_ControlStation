
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
        self.publisher_four_in_one      = self.create_publisher(Float32MultiArray, 'EL/four_in_one', 10)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):

        print('Science data test is running: "%d"' % self.i)

        # msg_log = DiagnosticStatus()
        # msg_log.name = 'Science data Test'
        # msg_log.level = self.i % 3
        # msg_log.message = 'Diagnostic Status Message from Science data Test : ' + str(self.i)
        # self.publisher_log.publish(msg_log)

        msg_float_32_multi = Float32MultiArray()

        msg_float_32_multi.data = [float(self.i * 3), float(self.i - 10)]
        self.publisher_mass.publish(msg_float_32_multi)

        msg_float_32_multi.data = [float(self.i), 
                                    float(self.i + 1),
                                    float(self.i + 2), 
                                    float(self.i + 3),
                                    float(self.i + 4),
                                    float(self.i + 5),
                                    float(self.i + 6),
                                    float(self.i + 7),
                                    float(self.i + 8),
                                    float(self.i + 9),
                                    float(self.i + 10),
                                    float(self.i + 11),
                                    float(self.i + 12),
                                    float(self.i + 13),
                                    float(self.i + 14),
                                    float(self.i + 15),
                                    float(self.i + 16),
                                    ]
        self.publisher_spectrometer.publish(msg_float_32_multi)

        msg_float_32_multi.data = [float(self.i), float(self.i + 10), float(self.i + 20)]
        self.publisher_npk.publish(msg_float_32_multi)

        msg_float_32_multi.data = [float(self.i), float(self.i + 1), float(self.i + 2), float(self.i + 3)]
        self.publisher_four_in_one.publish(msg_float_32_multi)

        # self.publisher_potentiometers.publish(msg_float_32_multi)
        # self.publisher_LED_confirm.publish(msg_float_32_multi)
        # self.publisher_HD_voltmeter.publish(msg_int_8)
        # self.publisher_HD_laser.publish(msg_bool)
        
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
