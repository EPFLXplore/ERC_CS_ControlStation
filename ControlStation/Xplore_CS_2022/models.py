from django.db import models

# Create your models here.
class RoverConfirmation(models.Model):
    received = models.BooleanField()

class TaskProgress(models.Model):
    state = models.PositiveSmallIntegerField()

class ScienceProgress(models.Model):
    state = models.PositiveSmallIntegerField()

class Exception(models.Model):
    string = models.TextField()
