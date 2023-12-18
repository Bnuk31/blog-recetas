from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
from django.db import models
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='articulo_imagenes/', blank=True, null=True)
class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    autor = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    texto = models.TextField()


class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    es_colaborador = models.BooleanField(default=False)
    es_miembro = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # Agregar related_name para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',
        help_text='Specific permissions for this user.',
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    ingredientes = models.TextField()
    instrucciones = models.TextField()

    def __str__(self):
        return self.titulo