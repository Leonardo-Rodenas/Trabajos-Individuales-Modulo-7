# Generated by Django 4.2.2 on 2023-06-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App1Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('borrado', models.BooleanField()),
            ],
            options={
                'db_table': 'app_1_etiqueta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='App1Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_vencimiento', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('borrado', models.BooleanField()),
            ],
            options={
                'db_table': 'app_1_tarea',
                'managed': False,
            },
        ),
    ]