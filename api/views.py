from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.decorators import action
from rest_framework.views import APIView
from customer.models import Customer
from inventory.models import Product
from cart.models import Cart
from rest_framework.response import Response
from .serializers import CustomerSerializer,ProductSerializer,BasketSerializer
from rest_framework import status
# Create your views here.
class CustomerListView(APIView):
    def get(self,reguest):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many= True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomerDetailView(APIView):
    def get(self,request,id,format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self,request,id,format= None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response("customer deleted",status=status.HTTP_204_NO_CONTENT)
    


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  



class AddProductToBasket(APIView):
    def post(self, request, basket_id, product_id):
        try:
            basket = Cart.objects.get(id=basket_id)
            product = Product.objects.get(id=product_id)
        except (Cart.DoesNotExist, Product.DoesNotExist):
            return Response({"message": "Basket or Product not found."}, status=status.HTTP_404_NOT_FOUND)

        basket.products.add(product)
        basket.save()

        serializer = BasketSerializer(basket)
        return Response(serializer.data, status=status.HTTP_200_OK) 




class BasketDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = BasketSerializer

    @action(detail=True, methods=['post'])
    def add_product(self, request, pk=None):
        basket = self.get_object()  # Retrieve the basket instance
        product_id = request.data.get('product_id')  # Retrieve the product ID from the request data

        try:
            product = Product.objects.get(pk=product_id)  # Retrieve the product instance
        except Product.DoesNotExist:
            return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        # Add the product to the basket (You should implement your logic here)
        basket.products.add(product)

        # You may want to update the basket total or do other operations here if needed

        # Serialize the updated basket and return it in the response
        serialized_basket = BasketSerializer(basket)
        return Response(serialized_basket.data)         

    
        
