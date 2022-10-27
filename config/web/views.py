from django.shortcuts import render


#IMPORTAR EL FORMULARIO A RENDER
from web.formularios.formularioPlatos import FormularioPlatos

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def Platos(request):

    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioRegistro':formulario
    }

    return render(request,'platos.html',datosParaTemplate)

