# Generated by Django 4.0.4 on 2022-04-18 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_tags_project_tags_alter_socialmedialink_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]