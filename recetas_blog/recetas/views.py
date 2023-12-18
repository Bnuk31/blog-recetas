from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic import DetailView  # Importa DetailView
from .models import Receta, Articulo, Comentario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import TuFormularioDeCreacionDeArticulo
from django.views.generic.edit import CreateView
class InicioView(View):
    def get(self, request):
        return render(request, 'recetas/inicio.html')

class DetalleRecetaView(DetailView):
    model = Receta
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
        recetas = Receta.objects.all()
        return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})

@login_required
def crear_articulo(request):
    if request.user.es_colaborador:
        # Lógica para crear un nuevo artículo
        return render(request, 'recetas/crear_articulo.html')
    else:
        return redirect('recetas:lista_recetas')
class CrearArticuloView(View):
    template_name = 'recetas/crear_articulo.html'
    form_class = TuFormularioDeCreacionDeArticulo  
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
@login_required
def comentar_articulo(request, articulo_id):
    # Lógica para agregar un comentario al artículo
    return redirect('recetas:lista_recetas')
class CrearArticuloView(CreateView):
    model = Articulo
    form_class = TuFormularioDeCreacionDeArticulo
    template_name = 'recetas/crear_articulo.html'
    success_url = '/recetas/'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)