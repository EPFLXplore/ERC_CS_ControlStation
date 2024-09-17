#!/usr/bin/env python3

"""
pkg:    wheels_commands
node:   NAV_interface_cs_gamepad
topics: 
        publish:    /CS/NAV_gamepad 
        subscribe:  
        
description:  

"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

#from evdev import InputDevice, categorize, ecodes
import evdev
from evdev import InputDevice, categorize, ecodes

import threading

class Inft_Timer():
    def __init__(self, t, target):
        self.t = t
        self.target = target
        self.thread = threading.Timer(self.t, self.handler)
    
    def handler(self):
        self.target()
        self.thread = threading.Timer(self.t, self.handler)
        self.thread.start()

    def start(self):
        self.thread = threading.Timer(self.t, self.handler)
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


class FakeGamepadPublisher(Node):
    def __init__(self):
        super().__init__('NAV_fake_cs_gamepad')
        self.axes = [0.0] * 8  # Assuming 8 axes
        self.buttons = [0] * 17  # Assuming 17 buttons

        self.NAV_gampad_pub = self.create_publisher(Joy, '/CS/NAV_gamepad', 10)

        timer_period = 0.1  # seconds
        self.timer = Inft_Timer(timer_period, self.timer_callback_pub)

        self.device_path = self.find_device_path()
        self.device = None

        if self.device_path:
            self.device = InputDevice(self.device_path)
            self.get_logger().info(f'Using device: {self.device}')
            self.timer.start()
    

    def timer_callback_pub(self):
        # send the event on a topic 
        joy_msg = Joy()
        joy_msg.header.stamp = self.get_clock().now().to_msg()
        joy_msg.axes = self.axes
        joy_msg.buttons = self.buttons

        self.NAV_gampad_pub.publish(joy_msg)

        # reset the value after the message sent
        self.axes = [0.0] * 8  # Assuming 8 axes
        self.buttons = [0] * 17  # Assuming 17 buttons



    def find_device_path(self):
        # You can modify this to match your joystick's name
        target_device_name = 'Microsoft Controller'
        print(evdev.list_devices())
        devices = [InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            print(device.name)
            if device.name == target_device_name:
                self.axis_code_list, self.axis_info_list = zip(
                            *device.capabilities()[3])
                return device.path
        self.get_logger().error(f"Device '{target_device_name}' not found.")
        return None

          

    def process_event(self):
        # handle game pad event and normalize the data between 0-1
        for event in self.device.read_loop():
            # print('event', event)
            
            # if event.code == 4:
            #     print(event)
            #     print('type ', event.type, 'code ', event.code, 'event value',event.value )

            if event.type == ecodes.EV_ABS:
                # print("evabs")
                ax_id = self.axis_code_list.index(event.code)  # get the axis id which represents the joystick being moved


               
                
                

                if ax_id == 0:
                    #val needs to be between -1  and 1
                    val = 2.0 * (float(event.value) - self.axis_info_list[ax_id].min) / (
                        self.axis_info_list[ax_id].max - self.axis_info_list[ax_id].min) - 1.0
                    self.axes[ax_id] = val
                else:
                    #val needs to be between 0  and 1
                    val = (float(event.value) - self.axis_info_list[ax_id].min) / (
                    self.axis_info_list[ax_id].max - self.axis_info_list[ax_id].min)
                
                    self.axes[ax_id] = val  # Update the corresponding axis value


        

            if event.type == ecodes.EV_KEY:
                # Define a mapping from the event code to the button index
                button_mapping = {
                    304: 0,
                    305: 1,
                    307: 2,
                    308: 3,
                    310: 4,
                    311: 5,
                    314: 6,
                    315: 7,
                    316: 8,
                    318: 9,
                    320: 10,
                    321: 11,
                    323: 12,
                    324: 13,
                    326: 14,
                    327: 15,
                    329: 16

                }

                button_index = button_mapping.get(event.code)
                if button_index is not None:
                    self.buttons[button_index] = event.value  # Update the corresponding button value
        



def main(args=None):
    rclpy.init(args=args)
    fake_gamepad = FakeGamepadPublisher()

    # Spin in a separate thread
    thread = threading.Thread(target=rclpy.spin, args=(fake_gamepad, ), daemon=True)
    thread.start()

    
    try:
        fake_gamepad.process_event()
    except KeyboardInterrupt:
        pass

    fake_gamepad.destroy_node()
    rclpy.shutdown()
    thread.join()

if __name__ == '__main__':
    main()