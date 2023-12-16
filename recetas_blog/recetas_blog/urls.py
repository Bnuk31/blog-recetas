from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recetas/', include('recetas.urls')),
    # Añade la siguiente línea para redirigir la ruta principal a la vista de lista de recetas
    path('', include('recetas.urls')),
]