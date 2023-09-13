import numpy
import random
import rclpy
from rclpy.node import Node

from std_msgs.msg         import Int8MultiArray, Int8, Int32, Int32MultiArray, Bool, String, Int16MultiArray, Int16, Float32MultiArray
from diagnostic_msgs.msg  import DiagnosticStatus

from avionics_interfaces.msg import FourInOne, Voltage, NPK, MassArray, SpectroResponse, MassCalibOffset

class ElecTestNode(Node):

    def __init__(self):
        super().__init__('elec_test_publisher')

        # Log publisher
        self.publisher_log = self.create_publisher(DiagnosticStatus, 'ROVER/CS_log', 10)

        self.publisher_mass             = self.create_publisher(MassArray, 'EL/mass', 10)
        self.publisher_spectrometer     = self.create_publisher(SpectroResponse, 'EL/spectro_response', 10)
        self.publisher_npk              = self.create_publisher(NPK, 'EL/npk', 10)
        # self.publisher_four_in_one      = self.create_publisher(Float32MultiArray, 'EL/four_in_one', 10)
        self.publisher_four_in_one      = self.create_publisher(FourInOne, 'EL/four_in_one', 10)

        self.subscription_mass_calib_container =        self.create_subscription(MassCalibOffset,'EL/container/mass_calib_offset', self.mass_calib_container,1)
        self.subscription_mass_calib_drill     =        self.create_subscription(MassCalibOffset,'EL/drill/mass_calib_offset', self.mass_calib_drill,1)

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

        mass = MassArray()
        mass.mass = [float(self.i) + 0.1, float(self.i) + 0.2, float(self.i) + 0.3, float(self.i) + 0.8]
        self.publisher_mass.publish(mass)

        spectro = SpectroResponse()
        spectro.data = [float(v) for v in numpy.random.rand(18)]
        
        self.publisher_spectrometer.publish(spectro)

        npk = NPK()
        npk.nitrogen = random.randint(0, 10)
        npk.phosphorus = random.randint(0, 10)
        npk.potassium = random.randint(0, 10)
        self.publisher_npk.publish(npk)

        # msg_float_32_multi.data = [float(self.i), float(self.i + 1), float(self.i + 2), float(self.i + 3)]
        fio = FourInOne()
        fio.temperature = float(self.i)
        fio.moisture = float(self.i + 1)
        fio.conductivity = float(self.i + 2)
        fio.ph = float(self.i + 3)

        self.publisher_four_in_one.publish(fio)

        # v = Voltage()
        # v.voltage = random.uniform(0, 10)
        # self.publisher_voltage.publish(v)

        # self.publisher_potentiometers.publish(msg_float_32_multi)
        # self.publisher_LED_confirm.publish(msg_float_32_multi)
        # self.publisher_HD_voltmeter.publish(msg_int_8)
        # self.publisher_HD_laser.publish(msg_bool)
        
        self.i += 1

    def mass_calib_container(self, msg):
        print("mass_calib_container: " + str(msg))
        return
    
    def mass_calib_drill(self, msg):
        print("mass_calib_drill: " + str(msg))
        return
    


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
