from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Profile
from .forms import ProfileForm


class Profiles(TemplateView):
    """User Profile View"""
    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = get_object_or_404(Profile, user__id=self.kwargs["pk"])
        context = {"profile": profile, "form": ProfileForm(instance=profile)}
        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a profile"""
    form_class = ProfileForm
    model = Profile
    template_name = 'profiles/edit_profile.html'  # Make sure this template exists

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user__id=self.kwargs["pk"])

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.user.id})

    def form_valid(self, form):
        messages.success(self.request, "Profile has been edited successfully!")
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user
