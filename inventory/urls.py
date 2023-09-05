from django.urls import path
from .views import upload_product,products_list,product_details,cart_view,edit_product_view

urlpatterns = [
    path('products/upload', upload_product, name="product_upload_view"),
    path('products/list', products_list, name='products_list_views'),
    path('products/<int:id>/', product_details, name='product_detail_view'),
    path('products/edit/<int:id>/', edit_product_view, name='edit_product_view'),


    ]


