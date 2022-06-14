from django.contrib import admin
from .models import Cliente, Producto

# Register your models here.
# Permite  administrarel modelo completo

admin.site.register(Cliente) 
admin.site.register(Producto) 