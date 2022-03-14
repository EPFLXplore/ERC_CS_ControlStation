import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ControlStation.settings')
django.setup()

from Xplore_CS_2022.models import *

#Initialise database objects
confirm = RoverConfirmation.objects.create(received = False) 
task_state = TaskProgress.objects.create(state = 0)
science_state = ScienceProgress.objects.create(state = 0)
exception = Exception.objects.create(string = 'All good.')

