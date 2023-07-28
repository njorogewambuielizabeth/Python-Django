from django.urls import path
from .views import upload_product,products_list,product_details


urlpatterns = [
    path('products/upload', upload_product, name="product_upload_view"),
    path('products/list', products_list, name='products_list_views'),
    path('products/<int:id>/', product_details, name='product_details_view'),

    ]
