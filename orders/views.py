from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
# Create your views here.



def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})



def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def edit_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('order_detail_view', id=id)
    else:
        form = OrderForm(instance=order)
    return render(request, "orders/edit_order.html", {"form": form})



def order_details(request, id):
    order = Order.objects.get(id=id)
    return render(request, "orders/order_detail.html",{"order": order})