
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from recetas.views import  Contacto, acerca_de

from django.views.generic import TemplateView

app_name = "recetas_blog"


urlpatterns = [
    path('', include('recetas.urls')),
    path('admin/', admin.site.urls),
    path('contacto/', Contacto.as_view(), name="contactanos"),
    path("acerca_de/", acerca_de, name="acerca_de"),   
    path('404/', TemplateView.as_view(template_name='404.html'), name='not_found'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)