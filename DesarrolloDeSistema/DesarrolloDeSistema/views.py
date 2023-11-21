# funciones a mostrar
from django.http import HttpResponse

def mostrar(request):
    return HttpResponse("Hello World!")