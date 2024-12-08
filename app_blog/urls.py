from . import views
from django.urls import path
from .views import AddReview, Reviews

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),

    path('review/', AddReview.as_view(), name='add_review'),

    path('index/', Reviews.as_view(), name='index'),
    
    path('review/<int:id>/', views.review_detail, name='review_detail'),



]
