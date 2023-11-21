# funciones a mostrar
from django.http import HttpResponse

def mostrar(request):
    return HttpResponse("<html><body><h1>Hello Elias!</h1></body></html>")

def parametro(request, edad):
    return HttpResponse(f"en el año 2070 vas a tener: {(2070 - 2023) + edad}")

