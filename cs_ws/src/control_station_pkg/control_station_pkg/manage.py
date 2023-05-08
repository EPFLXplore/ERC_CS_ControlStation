#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import rclpy
import time

from threading import Thread
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_settings.settings')
import django
django.setup()


import MVC_node.cs_node as cs

CONTROL_STATION = None

def main():

    global CONTROL_STATION

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_settings.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate  a virtual environment?"
        ) from exc
    print("http://127.0.0.1:8000/launcher")
    if(not rclpy.ok()):
        rclpy.init(args=sys.argv)
            
        CONTROL_STATION = rclpy.create_node("CONTROL_STATION")
        cs.CS(CONTROL_STATION)
    
    execute_from_command_line(sys.argv)


    # try:
    #     from MVC_node.cs_node import CS
    #     CONTROL_STATION = CS()
    #     print("imported")
    # except:
    #     print("import error")

    #     #rclpy.init(args=sys.argv)

    
    # #rclpy.spin(CONTROL_STATION.node)
    # t2 = Thread(target=rclpy.spin, args=(CONTROL_STATION.node))

    
    # t2.start()
    
    # rospy.init_node("csApp", anonymous=False)

# ============================================================================
# DEBUG
# class setup:
    
#     def __init__(self):
#         try:
#             from MVC_node.cs_node import CS
#         except:
#             print("import error")

#         #rclpy.init(args=sys.argv)

#         self.CONTROL_STATION = CS()
#         #rclpy.spin(self.CONTROL_STATION.node)


# ============================================================================


if __name__ == '__main__':
  main()
