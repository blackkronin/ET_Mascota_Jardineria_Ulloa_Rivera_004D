from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Boleta, Producto, Cliente, Ciudad

class FormularioProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','precio','stock','nombre']
        labels={
            'idProducto':'CÓDIGO PRODUCTO',
            'precio':'PRECIO',
            'stock':'STOCK',
            'nombre':'NOMBRE',
        }
        widgets = {
            'idProducto':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el código de producto...',
                    'id':'idProducto'
                }
            ),
            'precio':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el precio del producto...',
                    'id':'precio'
                }
            ),
            'stock':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el stock del producto...',
                    'id':'stock'
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del producto...',
                    'id':'nombre'
                }
            )
        }
class FormularioCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ['rutCliente','nombreCli','celular','direccion','correo','cod_ciud']
        labels = {
            'rutCliente':'RUT CLIENTE',
            'nombreCli':'NOMBRE DE CLIENTE',
            'celular':'TELEFONO CONTACTO',
            'direccion':'DIRECCIÓN',
            'correo':'CORREO CLIENTE',
            'cod_ciud':'CÓDIGO DE CIUDAD',
        }
        widgets={
            'rutCliente':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el rut del cliente...',
                    'id':'rutCliente'
                }
            ),
            'nombreCli':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del cliente...',
                    'id':'nombreCli'
                }
            ),
            'celular':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono celular del cliente...',
                    'id':'celular'
                }
            ),
            'direccion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la dirección del cliente',
                    'id':'direccion'
                }
            ),
            'correo':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el email del cliente...',
                    'id':'correo'
                }
            ),
            'cod_ciud':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Seleccione ciudad',
                    'id':'cod_ciud'
                }
            )
        }
class FormularioBoleta(ModelForm):
    class Meta:
        model = Boleta
        fields = ['idBoleta','descripcion','cantidad','preciototal','codProd','codCliente']
        labels = {
            'idBoleta':'ID DE LA BOLETA',
            'descripcion': 'DETALLE BOLETA',
            'cantidad':'CANTIDAD PRODUCTOS',
            'preciototal':'PRECIO TOTAL DE COMPRA',
            'codProd':'CÓDIGO DE PRODUCTO',
            'codCliente':'CÓDIGO DE CLIENTE',
        }
        widgets = {
            'idBoleta':forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el código de la boleta..',
                    'id':'idBoleta'
                }
            ),
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el detalle de la boleta..',
                    'id':'descripcion'
                }
            ),
            'cantidad':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la cantidad de productos comprados..',
                    'id':'cantidad'
                }
            ),
            'preciototal':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el precio total de la compra..',
                    'id':'preciototal'
                }
            ),
            'codProd':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Seleccione el código del producto',
                    'id':'codProd'
                }
            ),
            'codCliente':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Seleccione el código del cliente',
                    'id':'codCliente'
                }
            )
        }
