# Generated by Django 4.2.2 on 2023-06-24 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_1', '0002_remove_tarea_etiqueta_remove_tarea_usuario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False)),
                ('creada', models.DateTimeField(auto_now_add=True)),
                ('borrado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['estado'],
            },
        ),
    ]
