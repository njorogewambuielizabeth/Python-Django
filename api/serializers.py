from rest_framework import serializers
from customer.models import Customer
from inventory.models import Product
from cart.models import Cart
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =  "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'       