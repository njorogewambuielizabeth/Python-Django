from django.urls import path
from . import views

urlpatterns = [
    path('cart/add/', views.add_to_cart, name='add_to_cart_view'),
    path('cart/view/', views.cart_view, name='cart_view'),
    path('cart/edit/<int:id>/',views.edit_cart, name='edit_cart_view'),
    path('cart/<int:id>/',views.cart_details, name='cart_details_view'),


    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:cart_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
     path('update_quantity/<int:cart_id>/', views.update_quantity, name='update_quantity'),



    path('cart/', views.cart_view, name='cart_view'),
    path('update_quantity/<int:item_id>/', views.update_quantity, name='update_quantity'),
    path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'),
 
]
