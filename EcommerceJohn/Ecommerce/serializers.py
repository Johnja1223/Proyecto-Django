from .models import Profile, Pais, Departamentos, Ciudades, Domicilio, Categoria, SubCategoria, Producto, Descuento, \
    DetalleDescuento, FormadePago, EstadodeCompra, OrdendeCompra, CuponDescuento

from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group, User
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.serializers import (
    SerializerMethodField
)
from rest_framework import serializers


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    #id_categoria = CategorySerializer(many=False)
    class Meta:
        model = Producto
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = OrdendeCompra
        fields = ['id_user', 'id_producto', 'cantidad', 'id_forma_pago', 'id_estado_compra']

#CODIGO PARA ASIGNAR UN GRUPO DE USUARIOS AUTOMATICAMENTE AL CREAR UN USUARIO USANDO DJ_REST_AUTH
class CustomRegisterSerializer(RegisterSerializer):
    def create(self, request):
        user = super().create(request)
        group, created = Group.objects.get_or_create(name='Clientes')
        user.groups.add(group)
        user.save()
        return user

    def custom_signup(self, request, user):
        group, created = Group.objects.get_or_create(name='Clientes')#        user.groups.add(group)
        print(">usuario creado exitosamente")
        user.save()