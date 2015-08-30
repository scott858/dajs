from rest_framework import viewsets

from .serializers import ToDoSerializer, ProductSerializer
from todo.models import ToDo
from sports_store.models import Product


class ToDoViewset(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
