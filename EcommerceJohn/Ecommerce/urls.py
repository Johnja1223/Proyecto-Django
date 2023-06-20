from django.urls import path
from django.urls import re_path
from Ecommerce.views import UserListView
from .views import productListApi, OrderCreateAPIView, ProductCreateAPIView
from .views import categoriaListApi

urlpatterns = [
    path("listView/", UserListView.as_view(), name="listView"),
    path("", UserListView.as_view(), name="listView"),
]

app_name = 'Ecommerce'

urlpatterns = [
    re_path(r"^getproducts$", productListApi. as_view(), name="getproducts"),
    re_path(r"^getcategory$", categoriaListApi. as_view(), name="getcategory"),
    re_path(r"^createorder$", OrderCreateAPIView. as_view(), name="createorder"),
    re_path(r"^createproduct$", ProductCreateAPIView. as_view(), name="createproduct"),

]
