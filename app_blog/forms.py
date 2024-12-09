from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    """Form to create a review."""

    class Meta:
        model = Review
        fields = [
            'title',
            'genre',
            'images',
            'image_alt',
            'game_platform',
            'game_console',
            'review',
            'game_score',
        ]
        widgets = {
            'review': SummernoteWidget(),

            'genre': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'title': 'Game Title',
            'genre': 'Genre',
            'review': 'Write Review',
            'images': 'Game Image',
            'image_alt': 'Describe Game Image',
            'game_platform': 'Pick Game Platform',
            'game_console': 'Game Console Name',
            'game_score': 'Final Game Review Score',
        }


class CommentForm(forms.ModelForm):
    class Meta:

        model = Comment
        fields = ['body']

        widgets = {
            'review': SummernoteWidget(),

        }
