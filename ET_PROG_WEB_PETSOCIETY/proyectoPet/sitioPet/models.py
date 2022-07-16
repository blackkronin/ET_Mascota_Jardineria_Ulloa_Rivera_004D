from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ciudad (models.Model):
    idCiudad = models.IntegerField(primary_key=True,verbose_name="Código de la ciudad")
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la ciudad")
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=15, verbose_name="Código del producto")
    precio = models.IntegerField(verbose_name="Precio del producto")
    stock = models.IntegerField(verbose_name="Cantidad total de Producto(Bodega)")
    nombre = models.CharField(max_length=50, verbose_name="Nombre del producto a vender")
    fotoprod = models.ImageField(null=True,verbose_name="Imágen de los productos")
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    rutCliente = models.CharField(primary_key=True,max_length=10,verbose_name="Rut del Cliente(Consumidor)")
    nombreCli = models.CharField(max_length=50, verbose_name="Nombre del Cliente")
    celular = models.IntegerField(verbose_name="Número de celular Cliente")
    direccion = models.CharField(max_length=100, verbose_name="Número de casa y dirección pasajes,etc.")
    correo = models.EmailField(max_length=50,verbose_name="Correo Electrónico del Cliente",null=True)
    cod_ciud = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    def __str__(self):
        return self.rutCliente

class Boleta (models.Model):
    idBoleta = models.CharField(max_length=10,primary_key=True,verbose_name="Código de la boleta")
    descripcion = models.CharField(max_length=50,verbose_name="Descripción de la compra de objeto(s)")
    cantidad = models.IntegerField(verbose_name="Número de productos a comprar")
    preciototal = models.IntegerField(verbose_name="Precio de producto por cantidad")
    codProd = models.ForeignKey(Producto, on_delete=models.CASCADE)
    codCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return self.idBoleta

class EstadoCompra (models.Model):
    app_label = '<sitioPet>'
    idEstado = models.PositiveSmallIntegerField(primary_key=True,verbose_name="Id del estado de compra")
    estado = models.CharField(max_length=25,verbose_name="(En preparación,En despacho,Entregado)")
    def __str__(self):
        return self.estado

class Compra (models.Model):
    app_label = '<sitioPet>'
    idCompra = models.CharField(primary_key=True,max_length=10,verbose_name="Id de la compra")
    cod_estado = models.ForeignKey(EstadoCompra,on_delete=models.CASCADE)
    cod_bol = models.ForeignKey(Boleta, on_delete=models.CASCADE)

	
#### tienda

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='customer')
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address