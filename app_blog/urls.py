from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

from .views import (
    TemplateView,
    AddReview, Reviews,
    review_detail, DeleteReview,
    EditReview
)

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),  # Home page view

    path('review/', AddReview.as_view(), name='add_review'),  # Add review page

    # Changed from 'index' to 'reviews'
    path('reviews/', views.Reviews.as_view(), name='reviews'),

    path('review_detail/<int:id>/', views.review_detail,
         name='review_detail'),  # Review detail page

    path('delete/<int:pk>/', views.DeleteReview.as_view(),
         name='delete_review'),  # Delete review

    path('edit/<int:pk>/', views.EditReview.as_view(),
         name='edit_review'),  # Edit review


    
]
