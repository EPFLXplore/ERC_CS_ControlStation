from django.db import models

# Create your models here.
class RoverConfirmation(models.Model):
    received = models.BooleanField()

    def __str__(self):
        return str(self.received)

class TaskProgress(models.Model):
    state = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.state)

class Science(models.Model):
    sc_text = models.TextField()

    t1_hum = models.PositiveSmallIntegerField()
    t2_hum = models.PositiveSmallIntegerField()
    t3_hum = models.PositiveSmallIntegerField()

    mass = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.sc_text)

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


class Exception(models.Model):
    string = models.TextField()

    def __str__(self):
        return str(self.string)