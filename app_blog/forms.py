from django import forms

from djrichtextfield.widgets import RichTextWidget

from .models import Review


class Reviewform(forms.ModelForm):
    """   Form to create a review   """

    class Meta:
        model = Review
        fields = [

            'title',
            'genre',
            'review',
            'images',
            'image_alt',
            'game_platform',
            'game_console',
            'game_score',



        ]


review = forms.CharField(widget=RichTextWidget())

widgets = {

    'genre': forms.Textarea(attrs={'rows': 5}),

}

labels = {
    'title': 'Game Title', 
    'genre': 'Genre',
    'review': 'Write Review',
    'images': 'Game Image',
    'image_alt': 'Describe Game Image',
    'game_platform': 'Pick Game Platform',
    'game_console': 'Pick Game Console',
    'game_score': 'Final Game Review Score',
}
