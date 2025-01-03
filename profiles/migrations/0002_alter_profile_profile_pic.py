# Generated by Django 4.2.16 on 2025-01-03 02:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='blank-avatar-photo-place-holder_yvkwdr', max_length=255, verbose_name='image'),
        ),
    ]