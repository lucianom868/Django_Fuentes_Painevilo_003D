from django.urls import path
from .views import inicio, somos, galeria, registro, respuesta, crearUsuario, mostrarUsuario, modificarUsuario, eliminarUsuario, crearProducto, mostrarProducto, modificarProducto, eliminarProducto

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('somos/', somos, name="somos"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('respuesta/', respuesta, name="respuesta"),
    path('crearUsuario/', crearUsuario, name="crearUsuario"),
    path('mostrarUsuario/', mostrarUsuario, name="mostrarUsuario"),
    path('modificarUsuario/<id>', modificarUsuario, name="modificarUsuario"),
    path('eliminarUsuario/<id>', eliminarUsuario, name="eliminarUsuario"),
    path('crearProducto/', crearProducto, name="crearProducto"),
    path('mostrarProducto/', mostrarProducto, name="mostrarProducto"),
    path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),

    ]