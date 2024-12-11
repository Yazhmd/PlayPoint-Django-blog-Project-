from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Form to create a profile"""

    class Meta:
        model = Profile
        fields = ["profile_pic", "first_name", "last_name", "bio"]

        labels = {
            "Profile_pic": "Avatar",
            "first_name": "First Name",
            "last_name": "Last Name",
            "bio": "Bio",
        }
