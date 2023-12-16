from django.shortcuts import render
from .models import Receta

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})