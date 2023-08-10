from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ShipmentForm
from .models import Shipment
# Create your views here.


def create_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipment_list')
    else:
        form = ShipmentForm()
    return render(request, 'shipping/create_shipment.html', {'form': form})



def shipment_list(request):
    shipments = Shipment.objects.all()
    return render(request, 'shipping/shipment_list.html', {'shipments': shipments})


def edit_shipment(request, id):
    shipment = Shipment.objects.get(id=id)
    if request.method == "POST":
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
        return redirect('shipment_detail_view', id=id)
    else:
        form = ShipmentForm(instance=shipment)
    return render(request, "shipping/edit_shipment.html", {"form": form})



def shipment_details(request, id):
    shipment = Shipment.objects.get(id=id)
    return render(request, "shipping/shipping_detail.html",{"shipment": shipment})