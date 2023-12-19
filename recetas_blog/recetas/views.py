from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic import DetailView  # Importa DetailView
from .models import  Articulo, Comentario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import TuFormularioDeCreacionDeArticulo
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import UpdateView


class InicioView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'recetas/inicio.html', {'form': form})
    

class DetalleRecetaView(DetailView):
    model = Articulo
    template_name = 'recetas/detalle_receta.html'
    context_object_name = 'receta'
    
    
class SignupView(View):
    template_name = 'recetas/signup.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('recetas:crear_articulo')  # Redirige a la página de creación de artículo después de registrarse
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required, name='dispatch')
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('recetas:crear_articulo')  # Redirige a la página principal después de registrarse
        return render(request, self.template_name, {'form': form})
    

class ListaRecetasView(View):
    def get(self, request):
        recetas = Articulo.objects.all()
        return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})
    

@user_passes_test(lambda u: u.is_superuser)
class CrearArticuloView(View):
    template_name = 'recetas/crear_articulo.html'
    form_class = TuFormularioDeCreacionDeArticulo 
    success_url = reverse_lazy('recetas:lista_recetas') 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el artículo
            articulo = form.save(commit=False)
            # Asignar el usuario actual como autor del artículo
            articulo.autor = self.request.user
            articulo.save()
            return redirect('nombre_de_tu_url')
        return render(request, self.template_name, {'form': form})
    

class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = ["titulo",'contenido','categoria','imagen']
    template_name = "recetas/editar_articulo.html"
    
    
@login_required
def comentar_articulo(request, articulo_id):
    # Lógica para agregar un comentario al artículo
    return redirect('recetas:lista_recetas')
class CrearArticuloView(CreateView):
    model = Articulo
    form_class = TuFormularioDeCreacionDeArticulo
    template_name = 'recetas/crear_articulo.html'
    success_url = reverse_lazy('recetas:lista_recetas')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = self.request.user
            articulo.save()
            return redirect('recetas:lista_recetas')
        return render(request, self.template_name, {'form': form})