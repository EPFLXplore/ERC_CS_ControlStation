from django.urls import path

from . import views

urlpatterns = [
    path('python/',	views.python, name='python'),
    path('simple_function', views.simple_function)
]
