from django.db import models

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    ingredientes = models.TextField()
    instrucciones = models.TextField()

    def __str__(self):
        return self.titulo