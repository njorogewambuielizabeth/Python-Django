from django.urls import path
from . import views

urlpatterns = [
    path('reviews/create/', views.create_review, name='create_review'),
    path('reviews/list/', views.review_list, name='review_list_view'),
    path('reviews/edit/<int:id>/',views.edit_review, name='edit_review_view'),
    path('reviews/<int:id>/',views.review_details, name='review_detail_view'),
    # Add other URLs for review views if needed
]

