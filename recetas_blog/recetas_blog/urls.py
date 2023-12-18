from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recetas/', include('recetas.urls')), 
    path('', include('recetas.urls')),
]