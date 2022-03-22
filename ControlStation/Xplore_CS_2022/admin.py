from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(RoverConfirmation)
admin.site.register(TaskProgress)
admin.site.register(Science)
admin.site.register(Exception)

admin.site.register(Navigation)