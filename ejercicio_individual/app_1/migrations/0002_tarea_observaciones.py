# Generated by Django 4.2.2 on 2023-06-28 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
    ]
