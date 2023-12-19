from django.contrib import admin
from django.urls import include, path
from recetas.views import InicioView
urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('admin/', admin.site.urls),
    path('recetas/', include('recetas.urls')), 
   
]