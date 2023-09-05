from django.urls import path
from .views import CustomerListView,CustomerDetailView,ProductListView,ProductDetailView,AddProductToBasket,BasketDetailAPIView


urlpatterns = [
    path("customers/",CustomerListView.as_view(),name="customer_list_view" ),
    path("customers/<int:id>/",CustomerDetailView.as_view(),name="customer_detail_view" ),

    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('baskets/<int:basket_id>/add-product/<int:product_id>/', AddProductToBasket.as_view(), name='add-product-to-basket'),
    path('baskets/<int:pk>/', BasketDetailAPIView.as_view(), name='basket-detail'),
    path('baskets/<int:pk>/add-product/', BasketDetailAPIView.as_view(), name='basket-add-product'),

]