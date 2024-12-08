from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView , DetailView
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin


# HomePage view
class HomePage(TemplateView):
    """Displays home page"""
    template_name = 'base.html'


# Reviews List view (ListView)
class Reviews(ListView): 
    """ View all reviews """
    model = Review
    template_name = "app_blog/index.html"
    context_object_name = 'reviews'
    paginate_by = 6

    def get_queryset(self):
        """Override to apply custom filters (optional)"""
        return Review.objects.filter(status=1)


# Review Detail view
def review_detail(request, id):
    """Display details of a single review"""
    review = get_object_or_404(Review, id=id)
    return render(request, 'app_blog/review_detail.html', {'review': review})


# AddReview view (CreateView)
class AddReview(LoginRequiredMixin, CreateView):
    """Add review view"""
    template_name = 'app_blog/add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('add_review')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)
