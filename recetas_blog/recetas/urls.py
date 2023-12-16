from django.urls import path
from .views import lista_recetas

urlpatterns = [
    path('', lista_recetas, name='lista_recetas'),
]