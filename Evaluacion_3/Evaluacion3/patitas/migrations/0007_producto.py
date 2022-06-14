# Generated by Django 4.0.4 on 2022-06-13 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patitas', '0006_alter_cliente_rut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Codigo')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('precio', models.IntegerField(verbose_name='Precio')),
            ],
        ),
    ]