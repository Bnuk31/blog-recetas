from django.urls import path
from django.urls import include 
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import login_view
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from recetas.views import home_post, contacto, acerca_de, login_view
app_name ='recetas'

urlpatterns = [
    path('', home_post, name='home_post'),
    # path('admin/', admin.site.urls),
    path("home/", views.home_post, name="home_post"),
    path("post_realizado/", views.post_realizado, name="post_realizado"),
    path("post_detail/<int:post_id>", views.post_detail, name="post_detail"),
    path("comentario", views.comentar_posteo, name="comentar"),
    path("Borrar/<int:pk>", views.Borrar_Comentario.as_view(), name="borrar_comentario"),
    path("Modificar/<int:pk>", views.Modificar_Comentario.as_view(), name="modificar_comentario"),
    path("cargar/", views.Cargar_Post.as_view(), name="cargar_post"),
    path("registro/", views.registro, name="registro"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
]