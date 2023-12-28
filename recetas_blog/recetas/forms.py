from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Comentario, Post
from django.contrib.auth.forms import AuthenticationForm


class Formulario_Modificacion(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("texto",)


class Form_Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "titulo",
            "cuerpo",
            "imagen",
            "categoria_post",
        )
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categoria_post': forms.Select(attrs={'class': 'form-control'}),
        }
class FormularioRegistro(UserCreationForm):
    username = forms.CharField(
        label="Nombre de Usuario",
        widget=forms.TextInput(attrs={'class': 'form-control-registro'}),
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control-registro'}))
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control-registro'}),
    )
    password2 = forms.CharField(
        label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control-registro'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
