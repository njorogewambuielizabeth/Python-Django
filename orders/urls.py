from django.urls import path
from . import views

urlpatterns = [
    path('orders/create/', views.create_order, name='create_order_view'),
    path('orders/list/', views.order_list, name='order_list_view'),
    path('orders/edit/<int:id>/',views.edit_order, name='edit_order_view'),
    path('orders/<int:id>/',views.order_details, name='order_details_view'),
 
]


