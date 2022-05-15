# Generated by Django 4.0.4 on 2022-04-17 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informationsetup',
            old_name='phone_numer',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='article',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='project',
            name='is_visible',
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('visible', 'Visible'), ('published', 'Published')], default='visible', max_length=9, verbose_name='visibility'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('visible', 'Visible'), ('published', 'Published')], default='visible', max_length=9, verbose_name='visibility'),
        ),
    ]