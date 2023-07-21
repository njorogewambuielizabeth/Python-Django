from django.shortcuts import render
from .forms import ProductUploadForm

# Create your views here.
def upload_product(request):
    form = ProductUploadForm()
    return render(request,'inventory/product_upload.html',{'form':form})