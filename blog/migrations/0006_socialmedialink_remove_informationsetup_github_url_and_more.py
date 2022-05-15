# Generated by Django 4.0.4 on 2022-04-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_informationsetup_cv_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name="social media's name")),
                ('url', models.URLField(verbose_name='link to it')),
                ('icon_class', models.CharField(max_length=100, verbose_name='expressive font awesome icon class')),
            ],
            options={
                'verbose_name': 'social media link',
                'verbose_name_plural': 'social media links',
            },
        ),
        migrations.RemoveField(
            model_name='informationsetup',
            name='github_url',
        ),
        migrations.RemoveField(
            model_name='informationsetup',
            name='linkedin_url',
        ),
        migrations.RemoveField(
            model_name='informationsetup',
            name='twitter_url',
        ),
        migrations.AddField(
            model_name='article',
            name='icon_class',
            field=models.CharField(default='fa-solid fa-newspaper', max_length=100, verbose_name='expressive font awesome icon class'),
        ),
    ]
