from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('en/', views.home_en, name='home_en'),
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('servicios/', views.servicios, name='servicios'),
    path('reservas/', views.reservas, name='reservas'),
    path('galeria/', views.galeria, name='galeria'),
    path('paquetes/', views.paquetes, name='paquetes'),
]
