from rest_framework import serializers
from inventory.models import Product
from cart.models import Cart

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many = True)
    class Meta:
        model = Cart
        fields =  "__all__"

