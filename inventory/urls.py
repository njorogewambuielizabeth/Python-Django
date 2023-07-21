from django.urls import path
from .views import upload_product

urlpatterns = [
    path('products/upload', upload_product, name="product_upload_view"),
    ]