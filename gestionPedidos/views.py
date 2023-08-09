from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):
    
    if request.GET["prd"]:

        producto=request.GET["prd"]

        if len(producto)>20:
            mensaje="Texto de busqueda demasiado largo"

        else:
            
            articulos=Articulos.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query": producto})

    else:

        mensaje="No has introducido nada"

    return HttpResponse(mensaje)


def contacto(request):

    if request.method=="POST":

        miFormulario=FormularioContacto (request.POST)

        if miFormulario.is_valid():
            inForm=miFormulario.cleaned_data

            send_mail(inForm['asunto'], inForm['mensaje'], inForm.get('email', ''), )

