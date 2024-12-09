from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView, CreateView, ListView,
    DetailView, DeleteView, UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Review
from .forms import ReviewForm


# HomePage view
class HomePage(TemplateView):
    """Displays the home page."""
    template_name = 'base.html'


# AddReview view (CreateView)
class AddReview(LoginRequiredMixin, CreateView):
    """View to add a new review."""
    template_name = 'app_blog/add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews')   

    def form_valid(self, form):
        """Automatically assign the logged-in user to the review."""
        form.instance.user = self.request.user
        return super().form_valid(form)


# Reviews List view (ListView)
class Reviews(ListView):
    """View all approved reviews."""
    model = Review
    template_name = "app_blog/reviews.html"
    context_object_name = 'reviews'
    paginate_by = 6

    def get_queryset(self):
        """Fetch only reviews with status approved."""
        return Review.objects.filter(status=1)


# Review Detail view 
def review_detail(request, id):
    """Display details of a single review."""
    review = get_object_or_404(Review, id=id)
    return render(request, 'app_blog/review_detail.html', {'review': review})


# DeleteReview view (DeleteView)
class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View to delete a review."""
    model = Review
    template_name = 'app_blog/review_confirm_delete.html'
    success_url = reverse_lazy('reviews')   

    def test_func(self):
        """Ensure only the owner can delete their review."""
        return self.request.user == self.get_object().user


# EditReview view (UpdateView)
class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View to edit a review."""
    model = Review
    template_name = 'app_blog/edit_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('reviews')   

    def test_func(self):
        """Ensure only the owner can edit their review."""
        return self.request.user == self.get_object().user
