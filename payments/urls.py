from django.urls import path
from .views import create_payment,payment_list,payment_details,edit_payment

urlpatterns = [
    path('payments/create/', create_payment, name='create_payment_view'),
    path('payments/list/', payment_list, name='payment_list_view'),
    path('payments/edit/<int:id>/', edit_payment, name='edit_payment_view'),
    path('payments/<int:id>/', payment_details, name='payment_details_view'),
    # Add other URLs for views related to Payments if needed
]
