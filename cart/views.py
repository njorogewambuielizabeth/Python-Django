from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from .forms import CartForm
from .models import Cart
from rest_framework.views import APIView
from inventory.models import Product
from rest_framework.response import Response
from .serializers import CartSerializer
# Create your views here.

def cart(request):
    cart_items = Cart.objects.all()
    total_price = sum(item.price for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, cart_id):
    cart_item = Cart.objects.get(pk=cart_id)
    # Add logic to handle adding the item to the cart
    return redirect('cart')

def remove_from_cart(request, cart_id):
    cart_item = Cart.objects.get(pk=cart_id)
    cart_item.delete() 
    # Add logic to handle removing the item from the cart
    return redirect('cart')

def update_quantity(request, cart_id):
    cart_item = Cart.objects.get(pk=cart_id)
    new_quantity = int(request.POST.get('quantity', 1))
    if new_quantity > 0:
        cart_item.quantity = new_quantity
        cart_item.save()
    return redirect('cart')







def add_to_cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_view')
    else:
        form = CartForm()
    return render(request, 'cart/add_to_cart.html', {'form': form})




def edit_cart(request, id):
    cart = Cart.objects.get(id=id)
    if request.method == "POST":
        form = CartForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('cart_detail_view', id=cart.id)
    else:
        form = CartForm(instance=cart)
    return render(request, "cart/edit_cart.html", {"form": form})

def cart_details(request, id):
    cart = Cart.objects.get(id=id)
    return render(request, "cart/cart_detail.html",{"cart": cart})



def cart_view(request):
    cart_items = Cart.objects.all()
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)

def update_quantity(request, item_id):
    item = get_object_or_404(Cart, pk=item_id)
    if request.method == 'POST':
        new_quantity = int(request.POST['quantity'])
        item.quantity = new_quantity
        item.save()
    return redirect('cart_view')

def remove_item(request, item_id):
    item = get_object_or_404(Cart, pk=item_id)
    item.delete()
    return redirect('cart_view')


class AddToCart(APIView):
    def post(self, request,format=None):
        cart_id = request.data["cart_id"]
        product_id = request.data["product_id"]
        cart = Cart.objects.get(id = cart_id)
        product = Product.objects.get(id = product_id)
        updated_cart = cart.add_product(product)
        serializer = CartSerializer(updated_cart)
        return Response(serializer.data)





