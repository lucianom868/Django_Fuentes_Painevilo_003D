# Generated by Django 4.0.4 on 2022-06-12 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.IntegerField(max_length=9, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
    ]
