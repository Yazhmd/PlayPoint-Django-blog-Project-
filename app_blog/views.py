from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    TemplateView, CreateView, ListView,
    DetailView, DeleteView, UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Review, Comment
from .forms import ReviewForm, CommentForm


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

    #  comment submission
    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            
            # Assign the logged-in user to the comment
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.review = review
            comment.save()
            return redirect('review_detail', id=review.id)
    else:
        comment_form = CommentForm()

    return render(request, 'app_blog/review_detail.html', {
        'review': review,
        'comment_form': comment_form,
    })


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
