from rest_framework import serializers

from todo.models import ToDo
from sports_store.models import Product, Order


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ('action', 'done',)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'price',)


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'street', 'city', 'state',
                  'zip', 'country', 'giftwrap', 'products')
