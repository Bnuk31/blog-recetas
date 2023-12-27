from django.http import HttpResponse
from django.shortcuts import render

def contacto(request):
    return render(request, "contacto.html")

def acerca_de(request):
    return render(request, "acerca_de.html")