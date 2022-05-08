#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import rospy

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ControlStation.settings')
    try:
        from django.core.management import execute_from_command_line
        print("START LAUNCHER ==> http://127.0.0.1:8000/launcher")
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    rospy.init_node("CONTROL_STATION", anonymous=True)
    
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
