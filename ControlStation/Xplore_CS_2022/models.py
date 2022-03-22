from django.db import models


class RoverConfirmation(models.Model):
    # confirmation from the rover that it received an instruction
    received = models.BooleanField()

    def __str__(self):
        return str(self.received)


# Model for info on the current task progress:
class TaskProgress(models.Model):
    # Where are we currently in the task:
    #    - 0 if failure
    #    - 1 if success
    #    - 2 if checkpoint 
    state = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.state)


# Model for information coming from the Science subsystem
class Science(models.Model):
    # info on what is happening with the science bay
    sc_text = models.TextField()

    # fields for the humidity of samples in each tube
    t1_hum = models.PositiveSmallIntegerField()
    t2_hum = models.PositiveSmallIntegerField()
    t3_hum = models.PositiveSmallIntegerField()

    # total mass of the 2 tubes with the samples
    mass = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.sc_text)


# Model for info coming from the Navigation subsystem
class Navigation(models.Model):
    # fields for rover's position coordinates
    posX = models.FloatField()
    posY = models.FloatField()
    posZ = models.FloatField()

    # fields for rover's linear velocity coordinates
    linVelX = models.FloatField()
    linVelY = models.FloatField()
    linVelZ = models.FloatField()

    # fields for rover's angular velocity coordinates
    angVelX = models.FloatField()
    angVelY = models.FloatField()
    angVelZ = models.FloatField()


# Model for describing thrown exceptions
class Exception(models.Model):
    string = models.TextField()

    def __str__(self):
        return str(self.string)