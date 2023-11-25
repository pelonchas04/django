# funciones a mostrar
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from datetime import date

def mostrar(request):
    return HttpResponse("<html><body><h1>Hello Elias!</h1></body></html>")

def parametro(request, edad): # pasamos un parametro a la funcion que ingresamos (/<nombre_de_ventana>/parametro)
    return HttpResponse(f"en el año 2070 vas a tener: {(2070 - 2023) + edad}")

def plantillas(request):   # funcion que llama a plantillas (no es la más optima)

    fecha_del_dia_de_hoy = date.today()

    materias = ["Matematicas", "Ciencias Narurales", "Ciencias Sociales"]

    doc_externo = open("C:/Documentos/DESSARROLLO DE SOFTWARE/django/pruebas django y github/DesarrolloDeSistema/plantillas/index.html") # abrimos el documento html para esta funcion

    plantilla = Template(doc_externo.read()) # cargamos el documento (ya esta listo)

    doc_externo.close()  # cerramos el html porque ya esta guardado


    contexto = Context({"nombre_del_profesor": "Mario", "apellido_del_profesor": "Enriquez", "fecha_actual": fecha_del_dia_de_hoy, "materias": materias})  # por ahora no sirve ya que el html es simple

    documento = plantilla.render(contexto)  # le pasamos los cambios que realiza python sobre html

    return HttpResponse(documento)  # mostamos la plantilla 

def Plantillas_cargadores(request): # funcion que llama plantillas (optima y con cargadores #1)
    fecha_del_dia_de_hoy = date.today()

    materias = ["Fisica", "Quimica", "Programacion"]

    doc_externo = get_template("index.html")

    documento = doc_externo.render({"nombre_del_profesor": "Mario", "apellido_del_profesor": "Enriquez", "fecha_actual": fecha_del_dia_de_hoy, "materias": materias})

    return HttpResponse(documento)

def Plantillas_cargadores_2(request): # funcion que llama plantillas (optima y con cargadores #2
    fecha_del_dia_de_hoy = date.today()

    materias = ["Fisica", "Quimica", "Programacion"]

    return HttpResponse(render(request, "index.html", {"nombre_del_profesor": "Estuardo", "apellido_del_profesor": "Enriquez", "fecha_actual": fecha_del_dia_de_hoy, "materias": materias})) # el modulo shortcuts nos ayuda a eliminar más lines de codigo