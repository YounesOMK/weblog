# Generated by Django 4.0.4 on 2022-04-17 02:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('slug', models.SlugField(max_length=150, unique_for_date='publish')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_visible', models.BooleanField(default=True, verbose_name='is visible')),
                ('body', models.TextField(verbose_name='details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InformationSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, verbose_name='first name')),
                ('last_name', models.CharField(max_length=15, verbose_name='last_name')),
                ('phone_numer', models.CharField(max_length=13, verbose_name='phone number')),
                ('description', models.TextField(verbose_name='about me')),
                ('linkedin_url', models.URLField(verbose_name='linkedin profile link')),
                ('github_url', models.URLField(verbose_name='github url link')),
                ('twitter_url', models.URLField(verbose_name='twitter url link')),
                ('cv_file', models.FileField(upload_to='', verbose_name='pdf CV')),
            ],
            options={
                'verbose_name': 'My information setup',
                'verbose_name_plural': 'My information setup',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('slug', models.SlugField(max_length=150, unique_for_date='publish')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_visible', models.BooleanField(default=True, verbose_name='is visible')),
                ('decription', models.CharField(max_length=200, verbose_name='brief description')),
                ('link', models.URLField(blank=True, verbose_name='link to the project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
