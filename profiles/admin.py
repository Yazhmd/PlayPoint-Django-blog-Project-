from django.contrib import admin

from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "bio", "profile_pic")


admin.site.register(Profile, ProfileAdmin)
