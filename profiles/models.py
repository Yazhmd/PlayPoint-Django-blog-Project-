from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    User Profile Model
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    profile_pic = CloudinaryField(
        "image",
        default="blank-avatar-photo-place-holder_yvkwdr",
        transformation={
            "width": 300,
            "height": 300,
            "quality": 75,
            "crop": "fill",
        },
    )

    bio = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """Creates a user profile when a new user is created."""
    if created:
        Profile.objects.create(user=instance)


class Review(models.Model):
    """
    Review Model
    """

    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Assuming you want unique slugs for reviews
    slug = models.SlugField(unique=True)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
