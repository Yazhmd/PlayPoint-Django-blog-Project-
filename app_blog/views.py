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

from django.contrib import messages
from django.db.models import Q

from .models import Review, Comment
from .forms import ReviewForm, CommentForm


class HomePage(TemplateView):
    template_name = "base.html"


class AddReview(LoginRequiredMixin, CreateView):
    template_name = "app_blog/add_review.html"
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy("reviews")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Review Successfully Created!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Failed to create review. Please check the form for errors."
        )
        return super().form_invalid(form)


class Reviews(ListView):
    model = Review
    template_name = "app_blog/reviews.html"
    context_object_name = "reviews"
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return self.model.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(genre__icontains=query) |
                Q(game_platform__icontains=query) |
                Q(game_console__icontains=query)
            ).filter(status=0)
        else:
            return self.model.objects.filter(status=0)


def review_detail(request, id):
    review = get_object_or_404(Review, id=id)

    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.review = review
            comment.save()
            messages.success(
                request, "Comment submitted and awaiting approval.")
            return redirect("review_detail", id=review.id)
        else:
            messages.error(
                request, "Failed to submit comment. Please check the form for errors."
            )
    else:
        comment_form = CommentForm()

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


class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "app_blog/review_confirm_delete.html"
    success_url = reverse_lazy("reviews")

    def test_func(self):
        return self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Review Deleted.")
        return super().delete(request, *args, **kwargs)


class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    template_name = "app_blog/edit_review.html"
    form_class = ReviewForm
    success_url = reverse_lazy("reviews")

    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        messages.success(self.request, "Review Successfully Updated!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Failed to update review. Please check the form for errors."
        )
        return super().form_invalid(form)


def comment_edit(request, slug, comment_id):
    queryset = Review.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment_form.save()
            messages.success(request, "Comment Updated!")
            return HttpResponseRedirect(reverse("review_detail", args=[slug]))
        else:
            messages.add_message(request, messages.ERROR,
                                 "Error updating comment!")

    return render(
        request,
        "app_blog/edit_comment.html",
        {
            "comment_form": comment_form,
        },
    )


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Review.objects.all()
    print('Review objects: ', queryset)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )


    return HttpResponseRedirect(reverse("review_detail", args=[slug]))
