from django.shortcuts import render
import os
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def habitaciones(request):
    return render(request, 'core/habitaciones.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def reservas(request):
    return render(request, 'core/reservas.html')

def galeria(request):
    image_path = os.path.join(settings.BASE_DIR, 'core', 'static', 'images')
    image_names = [f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))]
    return render(request, 'core/galeria.html', {'image_names': image_names})

def paquetes(request):
    return render(request, 'core/paquetes.html')

def habitacion_simple(request):
    return render(request, 'core/habitacion_simple.html')

def habitacion_normal(request):
    return render(request, 'core/habitacion_normal.html')

def habitacion_matrimonial(request):
    return render(request, 'core/habitacion_matrimonial.html')


# def home_en(request):
#     return render(request, 'core/base_en.html')