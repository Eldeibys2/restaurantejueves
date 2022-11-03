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

    #PREGUNTAMOS SI EXISTE ALGUNA PETICION DE TIPO POST ASOCIADA A LA VISTA
    if request.method=='POST':
        #deberiamos capturar los datos del formulario
        datosDelFormulario=FormularioPlatos(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosPlato=datosDelFormulario.cleaned_data
            print(datosDelFormulario)
            print(datosPlato)


    return render(request,'platos.html',datosParaTemplate)

