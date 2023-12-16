from django.urls import path
from .views import ListaRecetasView
app_name = 'recetas'

urlpatterns = [
   
    path('', ListaRecetasView.as_view(), name='lista_recetas'),
]