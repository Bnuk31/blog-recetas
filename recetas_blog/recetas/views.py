from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic import DetailView  # Importa DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import DeleteView, UpdateView, CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import UpdateView
from .forms import Formulario_Modificacion, Form_Post
from .forms import FormularioRegistro
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from .models import *

def home_post(request):
    return render(request, "inicio.html")

def post(request):
    return render(request, "post.html")

def post_realizado(request):
    id_categoria = request.GET.get("id", None)
    antiguedad = request.GET.get("orden", None)
    alfabetico = request.GET.get("orden", None)
    ctx = {}

    if id_categoria:
        posteos = Post.objects.filter(categoria_post=id_categoria)
    else:
        if antiguedad == "asc":
            posteos = Post.objects.all().order_by("fecha_creacion")
        elif alfabetico == "a":
            posteos = Post.objects.all().order_by("titulo")
        elif alfabetico == "z":
            posteos = Post.objects.all().order_by("-titulo")
        else:
            posteos = Post.objects.all().order_by("-fecha_creacion")
    
    categorias = Categoria.objects.all()
    ctx["posteos"] = posteos
    ctx["categorias"] = categorias
    return render(
        request,
        "post/post.html",
        ctx,
    )


    
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    ctx = {"post": post}
    ctx['comentarios']=Comentario.objects.filter(post=post)
    return render(request, "post/post_detail.html", ctx)

def comentar_posteo(request):
    if request.method == 'POST':
        comentario = request.POST.get("comentario", None)
        if comentario:
            
            usuario = request.user
            post = request.POST.get("id_post", None)
            posteo = Post.objects.get(id=post)
            setear_comentario = Comentario.objects.create(
                usuario=usuario, post=posteo, texto=comentario
            )
        return redirect("recetas:post_detail", post_id=post)

class Borrar_Comentario(DeleteView):
    model = Comentario
    template_name = "comentarios/confirm_delete.html"
    success_url = reverse_lazy("recetas:post_realizado")


class Modificar_Comentario(UpdateView):
    model = Comentario
    form_class = Formulario_Modificacion
    template_name = "comentarios/modificar.html"
    success_url = reverse_lazy("recetas:post_realizado")
    

class Cargar_Post(CreateView):
    model = Post
    template_name = "post/cargar_post.html"
    form_class = Form_Post
    success_url = reverse_lazy("recetas:post_realizado")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.usuario = self.request.user
        return super(Cargar_Post, self).form_valid(form)


    
class Contacto(CreateView): 
    model=Contacto
    template_name= 'contacto.html'
    fields=['nombre','telefono','email','mensaje']
    success_url= reverse_lazy('recetas:home_post')
     
    def get_success_url(self):
        messages.success(self.request, 'Gracias por contactarnos')
        return super().get_success_url()
        

def acerca_de(request):
    return render(request, "acerca_de.html")
    
def registro(request):
    contexto = {}

    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            nombre_usuario = formulario.cleaned_data["username"]
            messages.success(request, f"Usuario {nombre_usuario} creado!!!")
            return redirect(reverse('recetas:home_post'))
    else:
        formulario = FormularioRegistro()

    contexto["form"] = formulario
    return render(request, "usuarios/registro.html", contexto)

def login_view(request):
    # Lógica para la vista de inicio de sesión
    if request.method == 'POST':
        # Obtener datos del formulario y realizar la autenticación
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirigir a la página deseada después del inicio de sesión
            return render(request, 'inicio.html')
        else:
            # Manejar el caso en que la autenticación falla
            return render(request, 'usuarios/login.html', {'error_message': 'Usuario o contraseña incorrectos.'})

    # Si es una solicitud GET, simplemente renderizar la página de inicio de sesión
    return render(request, 'usuarios/login.html')
def logout_view(request):
    # Lógica adicional de ser necesario
    logout(request)
    return render(request, 'usuarios/logout.html')