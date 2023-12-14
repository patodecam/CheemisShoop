from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Producto,Categoria,Boleta,Detalle_boleta
from .forms import ProductoForm, RegistroUserForm
from codigo.compra import Carrito

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def informacion(request):
    return render(request,'informacion.html')

def catalogo_productos(request):
    productos=Producto.objects.all()
    datos={'productos':productos}
    return render(request,'Catalogo_productos.html',datos)

@login_required
def agregar_producto(request):
    if request.method=="POST":
        prodcutoform =ProductoForm(request.POST, request.FILES) 
        if prodcutoform.is_valid():
            prodcutoform.save() 
            return redirect ('catalogo_productos')
    else:
        prodcutoform=ProductoForm()
    return render(request, 'agregar_producto.html', {'productoform' : prodcutoform})

@login_required
def eliminar(request,codigo):
    productoEliminado=Producto.objects.get(codigo=codigo)
    productoEliminado.delete()
    return redirect('catalogo_productos')

@login_required
def modificar(request,codigo):
    productoModificado=Producto.objects.get(codigo=codigo)
    datos={
        'form':ProductoForm(instance=productoModificado)
    }
    if request.method=="POST":
        formulario = ProductoForm(request.POST,request.FILES, instance= productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect('catalogo_productos')
    return render(request,'modificar_producto.html',datos)

#Registro de usuario

def registrar(request):
    data ={
        'form': RegistroUserForm()

    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], 
                                password= formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te Has Registrado Correctamente")
            return redirect('inicio')
        data['form']= formulario
    return render(request, 'registration/registrar.html', data)

#Carrito de compras
def carrito_compras(request):
    return render(request,'carrito.html')

def agregar_carrito(request,codigo):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(codigo=codigo)
    carrito_compra.agregar(producto=producto)
    return redirect('catalogo_productos')

def sumar_carrito(request,codigo):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(codigo=codigo)
    carrito_compra.agregar(producto=producto)
    return redirect('carrito_compras')

def eliminar_producto(request,codigo):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(codigo=codigo)
    carrito_compra.eliminar(producto=producto)
    return redirect('carrito_compras')

def restar_producto(request,codigo):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(codigo=codigo)
    carrito_compra.restar(producto=producto)
    return redirect('carrito_compras')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('carrito_compras')

#Detalle de compras.
def detalle_compras(request):
    return render(request,'detalle.html')

def generarBoleta(request):
    precio_total=0
    precio_envio=0
    precio_impuesto=0
    total_a_pagar=0
    username=""
    estado=""
    for key, value in request.session['carrito'].items():
        
        precio_total = round(precio_total + (int(value['precio']) * int(value['cantidad']))+precio_envio+precio_impuesto)
        precio_envio= round(precio_total*0.1)
        precio_impuesto=round(precio_total*0.19)
        username = request.user.username
        total_a_pagar=precio_total+precio_envio+precio_impuesto
        estado= "Procesando Pedido"
    boleta = Boleta(total = total_a_pagar,envio=precio_envio,impuestos=precio_impuesto,usuario=username,estado=estado)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(codigo = value['codigo'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = Detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
            # Descontar stock del inventario
            producto.stock -= cant
            producto.save()

    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total,
        'envio':boleta.envio,
        'impuesto':boleta.impuestos,
        'usuario':boleta.usuario,
        'estado':boleta.estado
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detalle.html',datos)

#Historial de compras
def historial(request):
    boleta=Boleta.objects.all().order_by('-fechaCompra')
    detalle=Detalle_boleta.objects.all()
    datos={'boleta':boleta,'detalle':detalle}
    return render(request,'historial.html',datos)