from django.urls import path
from .views import ListaRecetasView, DetalleRecetaView, comentar_articulo, InicioView
from .views import  CrearArticuloView, SignupView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignupView
app_name ='recetas'

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('lista/', ListaRecetasView.as_view(), name='lista_recetas'),
    path('detalle/<int:pk>/', DetalleRecetaView.as_view(), name='detalle_receta'),
     path('crear_articulo/', CrearArticuloView.as_view(), name='crear_articulo'),
    path('comentar_articulo/<int:articulo_id>/', comentar_articulo, name='comentar_articulo'),
    path('login/', LoginView.as_view(template_name='recetas/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='recetas/logout.html'), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]