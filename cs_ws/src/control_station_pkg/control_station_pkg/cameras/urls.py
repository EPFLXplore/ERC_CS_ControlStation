from django.urls import path
from . import views

urlpatterns = [
	path('<str:v_name>/', views.v_name, name='v_name'),
]