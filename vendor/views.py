from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import VendorForm
from .models import Vendor
# Create your views here.
def create_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'vendor/create_vendor.html', {'form': form})

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor/vendor_list.html', {'vendors': vendors})


def edit_vendor(request, id):
    vendor = Vendor.objects.get(id=id)
    if request.method == "POST":
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_detail_view', id=vendor.id)
    else:
        form = VendorForm(instance=vendor)
    return render(request, "vendor/edit_vendor.html", {"form": form})

def vendor_details(request, id):
    vendor = Vendor.objects.get(id=id)
    return render(request, "vendor/vendor_detail.html",{"vendor": vendor})