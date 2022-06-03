from django.shortcuts import render, redirect
from apps.cliente.models import Servicio
from apps.cliente.Formservicio import ServicioForm

# Create your views here.

def inicio(request):
    servicio = Servicio.objects.all().order_by('id')
    return render(request,'paginas/servicio.html', {'servicio': servicio})


def create(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ServicioForm()
        return render(request,'paginas/servicioForm.html', {'form': form})


def update(request,id):
    servicio = Servicio.objects.get(id=id)
    if request.method == 'GET':
        form = ServicioForm(instance=servicio)
    else:
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    return render(request, 'paginas/servicioForm.html', {'form': form})

def delete(request, id):
    servicio= Servicio.objects.get(id=id)
    servicio.delete()
    return redirect('inicio')




