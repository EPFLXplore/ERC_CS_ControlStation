from django.db import models

# Create your models here.
class RoverConfirmation(models.Model):
    name = models.TextField() #default="RoverConfirm"

    received = models.BooleanField(default = False)

    def __str__(self):
        return str(self.received)


class TaskProgress(models.Model):
    name = models.TextField(default = "TaskProgress")

    state = models.PositiveSmallIntegerField(default = -1)

    def __str__(self):
        return str(self.state)


class Science(models.Model):
    '''name = models.TextField(editable=False, default="Science")

    sc_text = models.TextField(default = "Nothing yet.")

    t1_hum = models.PositiveSmallIntegerField(default = -1)
    t2_hum = models.PositiveSmallIntegerField(default = -1)
    t3_hum = models.PositiveSmallIntegerField(default = -1)

    mass = models.PositiveSmallIntegerField(default = 0)
    '''

    name = models.TextField(default="Science")

    sc_text = models.TextField(null=True)

    t1_hum = models.PositiveSmallIntegerField(null=True)
    t2_hum = models.PositiveSmallIntegerField(null=True)
    t3_hum = models.PositiveSmallIntegerField(null=True)

    mass = models.PositiveSmallIntegerField(default = 0)

    def __str__(self):
        return str(self.sc_text)


class Navigation(models.Model):
    name = models.TextField(default="Navigation")

    # fields for rover's position coordinates
    posX = models.FloatField(default = 0.0)
    posY = models.FloatField(default = 0.0)
    posZ = models.FloatField(default = 0.0)

    # fields for rover's linear velocity coordinates
    linVelX = models.FloatField(default = 0.0)
    linVelY = models.FloatField(default = 0.0)
    linVelZ = models.FloatField(default = 0.0)

    # fields for rover's angular velocity coordinates
    angVelX = models.FloatField(default = 0.0)
    angVelY = models.FloatField(default = 0.0)
    angVelZ = models.FloatField(default = 0.0)

# incha'Allah on essaie ca un de ces quatres (:
''' 
    name = models.TextField(default="Navigation")

    # fields for rover's position coordinates
    posX = models.FloatField(null=True)
    posY = models.FloatField(null=True)
    posZ = models.FloatField(null=True)

    # fields for rover's linear velocity coordinates
    linVelX = models.FloatField(null=True)
    linVelY = models.FloatField(null=True)
    linVelZ = models.FloatField(null=True)

    # fields for rover's angular velocity coordinates
    angVelX = models.FloatField(null=True)
    angVelY = models.FloatField(null=True)
    angVelZ = models.FloatField(null=True)
'''

class Exception(models.Model):
    name = models.TextField(default = "Exception")

    string = models.TextField(default = "No exception yet")

    def __str__(self):
        return str(self.string)