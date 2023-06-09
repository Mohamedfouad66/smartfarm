# sensors_api/sensors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('temperature/', views.get_temperature, name='get_temperature'),
    path('humidity/', views.get_humidity, name='get_humidity'),
    path('soil/', views.get_soil_moisture, name='get_soil_moisture'),
    path('raindrop/', views.get_raindrop_status, name='get_raindrop_status'),
    path('pir/', views.get_pir_status, name='get_pir_status'),
]
