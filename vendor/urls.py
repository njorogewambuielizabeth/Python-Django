from django.urls import path
from . import views

urlpatterns = [
    path('vendor/create/', views.create_vendor, name='create_vendor'),
    path('vendor/list/', views.vendor_list, name='vendor_list'),
    path('vendor/edit/<int:id>/',views.edit_vendor, name='edit_vendor_view'),
    path('vendor/<int:id>/',views.vendor_details, name='vendor_details_view'),
 
]

