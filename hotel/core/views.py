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


# def home_en(request):
#     return render(request, 'core/base_en.html')