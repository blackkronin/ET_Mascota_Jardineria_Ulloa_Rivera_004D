from django.contrib import admin
from .models import Boleta,Ciudad,Cliente,Producto,Customer,Product,Order,OrderItem,ShippingAddress

# Register your models here.


admin.site.register(Producto)
admin.site.register(Ciudad)
admin.site.register(Boleta)
admin.site.register(Cliente)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)