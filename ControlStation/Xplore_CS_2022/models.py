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

class ScienceProgress(models.Model):
    state = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.state)

class Exception(models.Model):
    string = models.TextField()

    def __str__(self):
        return str(self.string)
