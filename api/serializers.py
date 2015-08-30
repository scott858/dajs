from rest_framework import serializers

from todo.models import ToDo
from sports_store.models import Product


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ('action', 'done',)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', )
