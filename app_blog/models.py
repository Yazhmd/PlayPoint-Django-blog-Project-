from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Options for game platforms and consoles


STATUS = ((0, "Draft"), (1, "Published"))

GAME_PLATFORM = [
    ('PC', 'PC'),
    ('PlayStation', 'PlayStation'),
    ('XBOX', 'XBOX'),
    ('Nintendo', 'Nintendo'),
    ('Other', 'Other'),
]

GAME_CONSOLE = [
    ('', 'None'),
]


def get_default_user():
    # Return None when no user is authenticated
    return None


class Review(models.Model):
    """
    A model to create and manage game reviews
    """
    user = models.ForeignKey(
        User, related_name='review_owner', on_delete=models.CASCADE,
        null=True, blank=True,
        default=get_default_user  # Set default user ID here
    )
    title = models.CharField(
        max_length=200, null=False, blank=False, default="")
    slug = models.SlugField(max_length=255, unique=True,
                            null=False, blank=True, default="")
    genre = models.CharField(
        max_length=500, null=False, blank=False, default="")
    review = models.TextField(
        max_length=10000, null=False, blank=False, default="")
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
        max_length=100, null=False, blank=False, default="")
    game_platform = models.CharField(
        max_length=50, choices=GAME_PLATFORM, default='PC')
    game_console = models.CharField(
        max_length=100, null=False, blank=False, default="")
    game_score = models.IntegerField(
        choices=[(i, str(i)) for i in range(11)],
        default=0  # Default value
    )
    posted_date = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('-posted_date',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    A model to create and manage comments on game reviews
    """
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
