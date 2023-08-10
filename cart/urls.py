from django.urls import path
from . import views

urlpatterns = [
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/view/', views.cart_view, name='cart_view'),
    path('cart/edit/<int:id>/',views.edit_cart, name='edit_cart_view'),
    path('cart/<int:id>/',views.cart_details, name='cart_details_view'),
 
]
