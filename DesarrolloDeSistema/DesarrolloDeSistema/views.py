# funciones a mostrar
from django.http import HttpResponse
from django.template import Template, Context
from datetime import date

def mostrar(request):
    return HttpResponse("<html><body><h1>Hello Elias!</h1></body></html>")

def parametro(request, edad):
    return HttpResponse(f"en el año 2070 vas a tener: {(2070 - 2023) + edad}")

def plantillas(request):   # funcion que llama a plantillas (no es la más optima)

    fecha_del_dia_de_hoy = date.today()

    materias = []

    doc_externo = open("C:/Documentos/DESSARROLLO DE SOFTWARE/django/pruebas django y github/DesarrolloDeSistema/plantillas/index.html") # abrimos el documento html para esta funcion

    plantilla = Template(doc_externo.read()) # cargamos el documento (ya esta listo)

    doc_externo.close()  # cerramos el html porque ya esta guardado

    contexto = Context({"nombre_del_profesor": "Mario", "apellido_del_profesor": "Enriquez", "fecha_actual": fecha_del_dia_de_hoy, "materias": materias})  # por ahora no sirve ya que el html es simple

    documento = plantilla.render(contexto)  # le pasamos los cambios que realiza python sobre html

    return HttpResponse(documento)  # mostamos la plantilla 

