from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Receta

class ListaRecetasView(View):
    def get(self, request):
        recetas = Receta.objects.all()
        return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})