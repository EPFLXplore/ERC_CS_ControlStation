#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys



def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djSettings.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    print("http://127.0.0.1:8000/launcher")
    execute_from_command_line(sys.argv)
    
    # rospy.init_node("CS2022", anonymous=False)

# ============================================================================
# DEBUG
class setup:
    
    def __init__(self):
        try:
            from src.cs_node import CS
        except:
            print("import error")

        self.CONTROL_STATION = CS()

# ============================================================================


if __name__ == '__main__':
  main()
