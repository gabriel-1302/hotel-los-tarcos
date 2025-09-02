from django.shortcuts import render

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
    return render(request, 'core/galeria.html')

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