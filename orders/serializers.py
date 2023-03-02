from rest_framework import serializers
from .models import Order, ProductsInOrder


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PrInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsInOrder
        fields = '__all__'
