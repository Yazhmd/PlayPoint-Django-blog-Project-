from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField

from cloudinary.models import CloudinaryField


from django_resized import ResizedImageField
from django.utils.text import slugify
from django.core.exceptions import ValidationError

STATUS = ((0, "Draft"), (1, "Published"))

GAME_PLATFORM = [
    ("PC", "PC"),
    ("PlayStation", "PlayStation"),
    ("XBOX", "XBOX"),
    ("Nintendo", "Nintendo"),
    ("Mobile", "Mobile"),
    ("Other", "Other"),
]

GAME_CONSOLE = [
    ("", "None"),
]


def get_default_user():
    # Return None when no user is authenticated
    return None


# Review Model---------------------------------------------------------------->


class Review(models.Model):
    user = models.ForeignKey(
        User,
        related_name="review_owner",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    genre = models.CharField(max_length=250)
    review = models.TextField(max_length=10000)
    images = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="app_blog/",
        force_format="WEBP",
        blank=True,
        null=True,
        default="app_blog/default_image.webp",
    )
    image_alt = models.CharField(max_length=100)

    game_platform = models.CharField(max_length=50, choices=GAME_PLATFORM, default="PC")
    game_console = models.CharField(max_length=100, null=False, blank=False, default="")

    game_score = models.IntegerField(
        choices=[(i, str(i)) for i in range(11)], default=0
    )

    posted_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ("-posted_date",)
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["-posted_date"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def clean(self):
        if not (0 <= self.game_score <= 10):
            raise ValidationError("Game score must be between 0 and 10.")
        super().clean()

    def __str__(self):
        return self.title


# Comment Model---------------------------------------------------------------->
class Comment(models.Model):

    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_comments"
    )
    body = models.TextField(max_length=10000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
