from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from django.views.generic import CreateView

from .models import Review

from .forms import Reviewform

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomePage(TemplateView):
    """Displays home page"""
    template_name = 'base.html'


class AddReview(LoginRequiredMixin, CreateView):
    """   Add review view     """
    template_name = 'app_blog/add_review.html'
    model = Review
    form_class = Reviewform
    # success_url = '/review/'
    success_url = reverse_lazy('add_review')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)
