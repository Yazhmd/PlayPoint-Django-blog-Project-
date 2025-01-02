from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages
from django.db.models import Q


from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# HomePage view


class HomePage(TemplateView):
    template_name = "base.html"


class AddReview(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "app_blog/add_review.html"
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy("reviews")
    success_message = "Review successfully created."

    def form_valid(self, form):
        """Automatically assign the logged-in user to the review."""
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Failed to create review. Please check the form for errors."
        )
        return super().form_invalid(form)


# Reviews List view (ListView)
class Reviews(ListView):
    model = Review
    template_name = "app_blog/reviews.html"
    context_object_name = "reviews"
    paginate_by = 6

    def get_queryset(self):
        """Fetch only reviews with status approved."""
        return Review.objects.filter(status=1)

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            review = self.model.objects.filter(
                Q(title__icontains=query)
                | Q(review__icontains=query)
                | Q(genre__icontains=query)
                | Q(game_platform__icontains=query)
                | Q(game_console__icontains=query)
            )

        else:
            review = self.model.objects.all()
        return review


def review_detail(request, id):
    review = get_object_or_404(Review, id=id)

    #  comment submission
    if request.method == "POST" and request.user.is_authenticated:
        print("Received a POST request")
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():

            # Assign the logged-in user to the comment
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.review = review
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )
            return redirect("review_detail", id=review.id)
    else:
        comment_form = CommentForm(data=request.POST)
        print("About to render template")

        comment_count = review.comments.filter(approved=True).count()

    return render(
        request,
        "app_blog/review_detail.html",
        {
            "review": review,
            "comment_form": comment_form,
            "comment_count": comment_count,
        },
    )


class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Review
    template_name = "app_blog/review_confirm_delete.html"
    success_url = reverse_lazy("reviews")
    success_message = "Review successfully deleted."

    def test_func(self):
        return self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Review successfully deleted.")
        return super().delete(request, *args, **kwargs)


class EditReview(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Review
    template_name = "app_blog/edit_review.html"
    form_class = ReviewForm
    success_url = reverse_lazy("reviews")
    success_message = "Review successfully updated."

    def test_func(self):
        return self.request.user == self.get_object().user
    


# Comment edit


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR,
                                 "Error updating comment!")

    return HttpResponseRedirect(reverse("review_detail", args=[slug]))


# Comment Delete


def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """
    post = get_object_or_404(Review, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("review_detail", args=[slug]))
