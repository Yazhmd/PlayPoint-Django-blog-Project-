from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages

from .models import Profile
from .forms import ProfileForm

# Create your views here.


class Profiles(TemplateView):
    """User Profile View"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = get_object_or_404(Profile, user=self.kwargs["pk"])
        context = {
            "profile": profile,
            "form": ProfileForm(instance=profile),
            "reviews": profile.user.reviews.all(),  # Fetch reviews associated with the user
        }
        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a profile"""

    form_class = ProfileForm
    model = Profile
    template_name = "profiles/edit_profile.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.kwargs["pk"])

    def form_valid(self, form):
        messages.success(self.request, "Profile has been edited successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        # Redirects to the profile page after editing the profile
        return f'/profiles/user/{self.kwargs["pk"]}/'

    def test_func(self):
        """Ensure that the logged-in user can only edit their own profile"""
        return self.request.user == self.get_object().user


def profile_view(request, user_id):
    """View to display a user's profile along with their reviews."""
    profile = get_object_or_404(Profile, user__id=user_id)
    reviews = profile.user.reviews.all()  # Fetch reviews associated with the user
    return render(
        request, "profiles/profile.html", {"profile": profile, "reviews": reviews}
    )
