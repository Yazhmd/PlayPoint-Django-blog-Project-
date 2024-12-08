from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Review


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
