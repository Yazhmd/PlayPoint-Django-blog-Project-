# Generated by Django 4.2.16 on 2025-01-02 17:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0019_alter_review_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='images',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
    ]