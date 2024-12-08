
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


from .models import Review
# Register your models here.


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'posted_date',
                    'game_platform', 'game_console', 'review', 'images',)

    search_fields = ['title', 'review', 'game_platform',]
    list_filter = ('status', 'posted_date',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('review',)
