from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


from django.core.exceptions import ValidationError

from django.urls import reverse

#3rd party

from taggit.managers import TaggableManager

STATUS_CHOICES = (
    ('visible', 'Visible'),
    ('invisible', 'Invisible'),
)    



class VisibleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='visible')




class Post(models.Model):


    title = models.CharField(_('title'), max_length=150)
    slug = models.SlugField(max_length=150, unique_for_date='publish')

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(_('visibility'), max_length=9, choices=STATUS_CHOICES, default='visible')

    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Article(Post):
    body = models.TextField(_('details'))
    icon_class = models.CharField(_('expressive font awesome icon class'), max_length=100, default='fa-solid fa-newspaper')

    objects = models.Manager()
    visible = VisibleManager()

    def get_absolute_url(self):
        return reverse('blog:article_detail', args= [
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug,
        ])

    



class Project(Post):
    decription = models.CharField(_('brief description'), max_length=200)
    link = models.URLField(_('link to the project'), blank=True)

class InformationSetup(models.Model):
    first_name = models.CharField(_('first name'), max_length=15)
    last_name = models.CharField(_('last_name'), max_length=15)
    phone_number = models.CharField(_('phone number'), max_length=13)
    description = models.TextField(_('about me'))

    # linkedin_url = models.URLField(_('linkedin profile link'), blank=True)
    # github_url = models.URLField(_('github url link'), blank=True)
    # twitter_url = models.URLField(_('twitter url link'), blank=True)

    cv_file = models.FileField(_('pdf CV'), blank=True)

    def clean(self):
        if InformationSetup.objects.exists() and not self.pk:
            raise ValidationError(_('You can only setup your information once'))

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'My information setup'
        verbose_name_plural = verbose_name


class SocialMediaLink(models.Model):
    name = models.CharField(_('social media\'s name'), max_length=20)
    url = models.URLField(_('link to it'), blank=True)
    icon_class = models.CharField(_('expressive font awesome icon class'), max_length=100)

    class Meta:
        verbose_name = 'social media link'
        verbose_name_plural = 'social media links'





class Comment(models.Model):
    

    objects = models.Manager()
    visible = VisibleManager()

    owner_pseudo_name = models.CharField(_('pseudo_name'), max_length=10)
    comment = models.TextField(_('comment'))

    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    status = models.CharField(_('visible'), max_length=9, choices=STATUS_CHOICES, default='visible')

    def __str__(self):
        return self.owner_pseudo_name




