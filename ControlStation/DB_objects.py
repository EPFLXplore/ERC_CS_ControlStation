import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ControlStation.settings')
django.setup()

from Xplore_CS_2022.models import *

#Initialise database objects
db_confirm = RoverConfirmation.objects.create(received = False) 
db_task_state = TaskProgress.objects.create(state = 0)
db_exception = Exception.objects.create(string = 'All good.')

db_science = Science.objects.create(sc_text="", t1_hum=0, t2_hum=0, t3_hum=0, mass=0)

db_navigation = Navigation.objects.create(posX=0, posY=0, posZ=0,
                                       linVelX=0, linVelY=0, linVelZ=0,
                                       angVelX=0, angVelY=0, angVelZ=0)


