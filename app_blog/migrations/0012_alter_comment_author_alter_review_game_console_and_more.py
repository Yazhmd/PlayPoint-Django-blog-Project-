# Generated by Django 4.2.16 on 2024-12-09 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_blog', '0011_alter_review_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='game_console',
            field=models.CharField(choices=[('None', 'None')], default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='review',
            name='image_alt',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='images',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='app_blog/default_image.webp', force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[400, None], upload_to='app_blog/'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['status'], name='app_blog_re_status_d8ec03_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['-posted_date'], name='app_blog_re_posted__6278ca_idx'),
        ),
    ]
