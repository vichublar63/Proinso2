from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClienteForm, EmpleadoForm,CategoriaForm,SubcategoriaForm,InsumosForm,VentasForm,ItemsForm
from django.template import RequestContext
from django.contrib import messages

# Create your views here.

def index(request):
    
    return render(request,'index.html')

def nuevo_cliente(request):
    clienteform=ClienteForm()

    if request.method=="POST":
        clienteform=ClienteForm(request.POST)
        if clienteform.is_valid():
            clienteform.save()
            print("Registro Guardado")
        else:
            print("Registro NO Guardado")
    return render(request,'forms/clientes.html',{'clienteform':clienteform})

def nuevo_empleado(request):
    empleadoform=EmpleadoForm()

    if request.method=="POST":
        empleadoform=EmpleadoForm(request.POST)
        if empleadoform.is_valid():
            empleadoform.save()
            messages.add_message(request, messages.INFO, 'Información Guardada')
        else:
            print("Registro NO Guardado")
    return render(request,'forms/empleados.html',{'empleadoform':empleadoform})

def categoria(request):
    categoriaform=CategoriaForm()

    if request.method=="POST":
        categoriaform=CategoriaForm(request.POST)
        if categoriaform.is_valid():
            categoriaform.save()
            print("Registro Guardado")
        else:
            print("Registro NO Guardado")
    return render(request,'forms/categoria_insumo.html',{'categoriaform':categoriaform})


def subcategoria(request):
    subcategoriaform=SubcategoriaForm()

    if request.method=="POST":
        subcategoriaform=SubcategoriaForm(request.POST)
        if subcategoriaform.is_valid():
            subcategoriaform.save()
            print("Registro Guardado")
        else:
            print("Registro NO Guardado")
    return render(request,'forms/subcategoria_insumo.html',{'subcategoriaform':subcategoriaform})

def insumos(request):
    insumosform=InsumosForm()

    if request.method=="POST":
        insumosform=InsumosForm(request.POST)
        if insumosform.is_valid():
            insumosform.save()
            print("Registro Guardado")
        else:
            print("Registro NO Guardado")
    return render(request,'forms/insumos.html',{'insumosform':insumosform})

def ventas(request):
    ventasform=VentasForm()

    if request.method=="POST":
        ventasform=VentasForm(request.POST)
        if ventasform.is_valid():
            ventasform.save()
            messages.add_message(request, messages.INFO, 'Venta Guardada')
        else:
            print("Registro NO Guardado")
    return render(request,'forms/ventas.html',{'ventasform':ventasform})

def items(request):
    itemsform=ItemsForm()

    if request.method=="POST":
        itemsform=ItemsForm(request.POST)
        if itemsform.is_valid():
            itemsform.save()
            messages.add_message(request, messages.INFO, 'Producto Agregado')
        else:
            print("Registro NO Guardado")
    return render(request,'forms/items.html',{'itemsform':itemsform})

