# Generated by Django 4.2.16 on 2024-12-10 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0016_alter_review_game_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.CharField(max_length=250),
        ),
    ]