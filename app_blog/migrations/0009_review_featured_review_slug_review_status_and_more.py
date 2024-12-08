# Generated by Django 4.2.16 on 2024-12-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0008_alter_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
