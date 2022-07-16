from rest_framework import serializers
from sitioPet.models import Cliente 

class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cliente
        fields =['rutCliente', 'nombreCli','celular','direccion','correo', 'cod_ciud']