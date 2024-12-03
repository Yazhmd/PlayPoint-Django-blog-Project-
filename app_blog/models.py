from django.db import models

from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Options for game platforms and consoles


GAME_PLATFORM = [
    ('PC', 'PC'),
    ('PlayStation', 'PlayStation'),
    ('XBOX', 'XBOX'),
    ('Nintendo', 'Nintendo'),
]

GAME_CONSOLE = [
    ('', 'None'),
]


class Review(models.Model):
    """
    A model to create and manage game reviews
    """

    user = models.ForeignKey(
        User, related_name='review_owner', on_delete=models.CASCADE,
        null=True,
        blank=True,

    )

    title = models.CharField(max_length=200, null=False,
                             blank=False, default="Untitled")
    description = models.CharField(
        max_length=500, null=False, blank=False, default="No description provided"
    )
    review = RichTextField(max_length=10000, null=False,
                           blank=False, default="No review content provided.")
    images = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to='app_blog/',
        force_format='WEBP',
        blank=False,
        null=False,
        default=''
    )
    image_alt = models.CharField(
        max_length=100, null=False, blank=False, default="No image description available"
    )
    game_platform = models.CharField(
        max_length=50, choices=GAME_PLATFORM, default='PC'
    )
    game_console = models.CharField(
        max_length=50, choices=GAME_CONSOLE, default=''
    )
    game_score = models.IntegerField(default=0)
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-posted_date',)

    def __str__(self):
        return self.title
