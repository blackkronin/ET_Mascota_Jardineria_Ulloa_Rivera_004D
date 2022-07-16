from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from django.views.decorators import csrf
from .utils import cookieCart, cartData, guestOrder
from .models import Boleta,Ciudad,Cliente,Producto,Customer,Product,Order,OrderItem,ShippingAddress
from .forms import FormularioBoleta,FormularioCliente,FormularioProducto
# Create your views here.

def index(request):
    return render (request, 'index.html')

def somos4(request):
    return render (request, 'somos4.html')

def indexapi(request):
    return render (request,'indexapi.html' )

def indexpruebahtmlcontacto(request):
    return render (request,'indexpruebahtmlcontacto.html' )

def registerpets(request):
    return render (request,'registerpets.html' )

def indeximc(request):
    return render (request,'index-imc.html' )

def index1(request):
    return render (request,'index1.html' )

def logIn(request):
    return render (request,'login.html')

def mostrardatos (request):
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()
    boletas = Boleta.objects.all()
    datos = {
        'productos' : productos,
        'clientes' : clientes,
        'boletas' : boletas,
    }
    return render(request , 'mostrar_datos.html',datos)

def form_producto(request):
    producto_form = FormularioProducto() 
    if request.method == 'POST':
        producto_form = FormularioProducto(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('mostrardatos')
    else:
        producto_form = FormularioProducto()
    datos = {'producto_form': producto_form}
    return render(request, 'form_crear_prod.html', datos)


def form_mod_prod(request, id):
    product = Producto.objects.get(idProducto=id)
    datos = {
        'form_mod_prod': FormularioProducto(instance = product)
    }
    if request.method=='POST':
        form_mod_prod = FormularioProducto(data=request.POST, instance = product)
        if form_mod_prod.is_valid():
            form_mod_prod.save()
            return redirect ('mostrardatos')
    return render(request, 'form_modi_prod.html', datos)


def form_del_prod(request,id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect('mostrardatos')


def form_cliente(request): 
    cliente_form = FormularioCliente()
    if request.method=='POST':
        cliente_form = FormularioCliente(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('mostrardatos')
    else:
        cliente_form = FormularioCliente()
    datos = {'cliente_form': cliente_form}
    return render(request, 'form_crear_cli.html', datos)


def form_mod_cli(request, id):
    p_cliente = Cliente.objects.get(rutCliente=id)
    datos = {
        'cliente_mod_form': FormularioCliente(instance = p_cliente)
    }
    if request.method=='POST':
        cliente_mod_form = FormularioCliente(data=request.POST, instance = p_cliente)
        if cliente_mod_form.is_valid():
            cliente_mod_form.save()
            return redirect ('mostrardatos')
    return render(request, 'form_mod_cli.html', datos)


def form_del_cli(request,id):
    client = Cliente.objects.get(rutCliente=id)
    client.delete()
    return redirect('mostrardatos')

def form_boleta(request): 
    boleta_form = FormularioBoleta()
    if request.method=='POST':
        boleta_form = FormularioBoleta(request.POST)
        if boleta_form.is_valid():
            boleta_form.save()
            return redirect ('mostrardatos')
    else:
        boleta_form = FormularioBoleta()
    datos = {'boleta_form': boleta_form}
    return render(request, 'form_crear_bole.html', datos)


def form_mod_boleta(request, id):
    boleta = Boleta.objects.get(idBoleta=id)
    datos = {
        'boleta_mod_form': FormularioBoleta(instance = boleta)
    }
    if request.method=='POST':
        boleta_mod_form = FormularioBoleta(data=request.POST, instance = boleta)
        if boleta_mod_form.is_valid():
            boleta_mod_form.save()
            return redirect ('mostrardatos')
        
    return render(request, 'form_mod_bole.html', datos)


def form_del_bole(request,id):
    boleta = Boleta.objects.get(idBoleta=id)
    boleta.delete()
    return redirect('mostrardatos')

####################CARRITO

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)