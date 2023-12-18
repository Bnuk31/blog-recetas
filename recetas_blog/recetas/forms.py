from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from .models import Articulo

class TuFormularioDeCreacionDeArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'imagen']  # Ajusta los campos según tus modelos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese una dirección de correo electrónico válida.')

    class Meta:
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('email', 'es_colaborador', 'es_miembro',)