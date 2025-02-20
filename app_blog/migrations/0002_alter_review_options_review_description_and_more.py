# Generated by Django 4.2.16 on 2024-12-03 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app_blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="review",
            options={"ordering": ("-posted_date",)},
        ),
        migrations.AddField(
            model_name="review",
            name="description",
            field=models.CharField(default="No description provided", max_length=500),
        ),
        migrations.AddField(
            model_name="review",
            name="game_console",
            field=models.CharField(choices=[("", "None")], default="", max_length=50),
        ),
        migrations.AddField(
            model_name="review",
            name="game_platform",
            field=models.CharField(
                choices=[
                    ("PC", "PC"),
                    ("PlayStation", "PlayStation"),
                    ("XBOX", "XBOX"),
                    ("Nintendo", "Nintendo"),
                ],
                default="PC",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="game_score",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="review",
            name="image_alt",
            field=models.CharField(
                default="No image description available", max_length=100
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="images",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                default="",
                force_format="WEBP",
                keep_meta=True,
                quality=75,
                scale=None,
                size=[400, None],
                upload_to="app_blog/",
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="posted_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="review",
            name="review",
            field=djrichtextfield.models.RichTextField(
                default="No review content provided.", max_length=10000
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="title",
            field=models.CharField(default="Untitled", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="review",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review_owner",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
