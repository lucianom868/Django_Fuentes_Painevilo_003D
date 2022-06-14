from xml.etree.ElementTree import tostring
from django.shortcuts import redirect, render
from django.views.decorators import csrf
from patitas.forms import ClienteForm, ProductoForm
from .models import Cliente, Producto

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def somos(request):
    return render(request,'somos.html')

def galeria(request):
    return render(request,'galeria.html')

def registro(request):   
    return render(request,'registro.html')

def respuesta(request):
    if request.method == 'POST':
        return render(request,'respuesta.html')

def crearUsuario(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('mostrarUsuario')
    else:
        cliente_form = ClienteForm()
    return render(request, 'crearUsuario.html', {'cliente_form' : cliente_form})
   
def mostrarUsuario(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes' : clientes
    }
    return render(request, 'mostrarUsuario.html', datos)  

def modificarUsuario(request, id):
    clientes = Cliente.objects.get(rut=id)
    datos ={
        'form': ClienteForm(instance=clientes)
    }
    if request.method=='POST':
        formulario = ClienteForm(data = request.POST, instance=clientes)
        if formulario.is_valid: 
            formulario.save()
            return redirect('mostrarUsuario')
    return render(request, 'modificarUsuario.html', datos)

def eliminarUsuario(request, id):
    clientes = Cliente.objects.get(rut=id)
    clientes.delete()
    return redirect('mostrarUsuario')

    
def crearProducto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('mostrarProducto')
    else:
        producto_form = ProductoForm()
    return render(request, 'crearProducto.html', {'producto_form' : producto_form})


def mostrarProducto(request):
    productos = Producto.objects.all()
    datos = {
        'productos' : productos
    }
    return render(request, 'mostrarProducto.html', datos)

def modificarProducto(request,id):
    productos = Producto.objects.get(codigo=id)
    datos ={
        'form': ProductoForm(instance=productos)
    }
    if request.method=='POST':
        formulario = ProductoForm(data = request.POST, instance=productos)
        if formulario.is_valid(): 
            formulario.save()
            return redirect('mostrarProducto')
    return render(request,'modificarProducto.html', datos)

def eliminarProducto(request, id): 
    productos = Producto.objects.get(codigo=id)
    productos.delete()
    return redirect('mostrarProducto')