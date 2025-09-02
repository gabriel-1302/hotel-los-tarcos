from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('en/', views.home_en, name='home_en'),
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('habitaciones/simple/', views.habitacion_simple, name='habitacion_simple'),
    path('habitaciones/normal/', views.habitacion_normal, name='habitacion_normal'),
    path('habitaciones/matrimonial/', views.habitacion_matrimonial, name='habitacion_matrimonial'),
    path('servicios/', views.servicios, name='servicios'),
    path('reservas/', views.reservas, name='reservas'),
    path('galeria/', views.galeria, name='galeria'),
    path('paquetes/', views.paquetes, name='paquetes'),
]
