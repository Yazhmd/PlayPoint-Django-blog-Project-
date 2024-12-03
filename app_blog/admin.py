
from django.contrib import admin
from .models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (

        'title',
        'game_platform',
        'game_console',
        'review',
        'images',

    )

    list_filter = ('game_platform',)
