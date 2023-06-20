from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
# GenericAPIView
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView
)
from .serializers import ProductSerializer, CategorySerializer,  OrderSerializer
from .models import Profile, Pais, Departamentos, Ciudades, Domicilio, Categoria, SubCategoria, Producto, Descuento, \
    DetalleDescuento, FormadePago, EstadodeCompra, OrdendeCompra, CuponDescuento

from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
 
# Create your views here.
class UserListView(ListView):
    model = User  
    template_name = 'user_list.html'  
    context_object_name = 'object_list'  
    paginate_by = 10 
    queryset = User.objects.all()  
    ordering = ['username']  


def signup(request):
    return render(request, "registration/signup.html",{})


@permission_classes((AllowAny, ))
class productListApi(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Producto.objects.all().order_by('nombreProducto')
    #queryset = Producto.objects.filter(precio__gte=240000)

@permission_classes((AllowAny, ))
class categoriaListApi(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Categoria.objects.all().order_by('nombreCategoria')


@permission_classes((AllowAny, ))
class OrderCreateAPIView(CreateAPIView):
    queryset = OrdendeCompra.objects.all()
    serializer_class = OrderSerializer
    permission_required = 'Ecommerce.add_ordendecompra'


@permission_classes((AllowAny, ))
class ProductCreateAPIView(CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer
    permission_required = 'Ecommerce.add_producto'