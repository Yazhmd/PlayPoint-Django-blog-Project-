from . import views
from django.urls import path
from .views import AddReview

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    
    path('review/', AddReview.as_view(), name='add_review'),
]
