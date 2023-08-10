from django.urls import path
from . import views

urlpatterns = [
    path('shipments/create/', views.create_shipment, name='create_shipment'),
    path('shipments/list/', views.shipment_list, name='shipment_list_view'),
   path('shipments/edit/<int:id>/',views.edit_shipment, name='edit_shipment_view'),
    path('shipments/<int:id>/',views.shipment_details, name='shipment_details_view'),
 
]
