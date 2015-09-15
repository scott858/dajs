from rest_framework import viewsets

from .serializers import ToDoSerializer, ProductSerializer, OrderSerializer
from todo.models import ToDo
from sports_store.models import Product, Order


class ToDoViewset(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
