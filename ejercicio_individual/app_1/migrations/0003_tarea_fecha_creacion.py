# Generated by Django 4.2.2 on 2023-06-30 00:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_tarea_observaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]