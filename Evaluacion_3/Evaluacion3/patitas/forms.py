from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from . models import Cliente, Producto

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'email']
        labels ={
            'rut': 'Rut',
            'nombre': 'Nombre',
            'email': 'Email',
        }
        widgets = {
            'rut' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su rut',
                    'id' : 'rut'
                }
            ),
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'ingrese su nombre',
                    'id' : 'nombre'
                }
            ),
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su email',
                    'id' : 'email'
                }
            )
        }

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'descripcion', 'precio', 'imagen']
        #imagen = forms.ImageField(label="Imagen", widget=forms.FileInput(attrs={'class':'form-control', 'placeholder':'Ingrese imagen del producto', 'id':'imagen'}))
        
        labels ={
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'precio' : 'Precio',
            'imagen' : 'Imagen',
        }
        widgets = {
            'codigo' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese codigo producto',
                    'id' : 'codigo'
                }
            ),
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'ingrese nombre producto',
                    'id' : 'nombre'
                }
            ),
            'descripcion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese descripcion del producto',
                    'id' : 'descripcion'
                }
            ),
            'precio' : forms.NumberInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese precio del producto',
                    'id' : 'precio'
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese imagen del producto',
                    'id' : 'imagen'
                }
            )
        }