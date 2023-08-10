from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CartForm
from .models import Cart
# Create your views here.
def add_to_cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_view')
    else:
        form = CartForm()
    return render(request, 'cart/add_to_cart.html', {'form': form})

def cart_view(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart/cart_view.html', {'cart_items': cart_items})


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