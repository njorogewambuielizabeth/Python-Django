from django.urls import path
from . import views

urlpatterns = [
    path('notifications/create/', views.create_notification, name='create_notification'),
    path('notifications/list/', views.notification_list, name='notification_list_view'),
    path('notifications/edit/<int:id>/',views.edit_notification, name='edit_notification_view'),
    path('notifications/<int:id>/', views.notification_details, name='notification_details_view'),

 
  
]
