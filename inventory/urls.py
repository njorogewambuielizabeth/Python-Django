from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_product,products_list,product_details,cart_view,edit_product_view

urlpatterns = [
    path('products/upload', upload_product, name="product_upload_view"),
    path('products/list', products_list, name='products_list_views'),
    path('products/<int:id>/', product_details, name='product_detail_view'),
     path('cart/', cart_view, name='cart_page'), 
    path('products/edit/<int:id>/', edit_product_view, name='edit_product_view'),


    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

