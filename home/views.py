from django.shortcuts import render

from django.views.generic import ListView

from app_blog.models import Review

# Create your views here.


class Index(ListView):

    template_name = "home/index.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        return self.model.objects.all()[:3]
