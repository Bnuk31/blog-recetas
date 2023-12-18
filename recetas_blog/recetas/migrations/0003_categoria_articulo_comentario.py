# Generated by Django 5.0 on 2023-12-17 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.usuario')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.articulo')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.usuario')),
            ],
        ),
    ]
