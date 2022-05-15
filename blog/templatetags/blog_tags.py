from django import template

from django.utils.safestring import mark_safe
from django.db.models import Count

from ..models import Article, InformationSetup, SocialMediaLink

import markdown
from taggit.models import Tag

register = template.Library()

@register.filter(name='markdown')
def markown_format(text):
    return mark_safe(markdown.markdown(text, extensions=['markdown.extensions.codehilite']))



@register.filter(name='count_articles')
def count_articles_for_tag(tag):
    count = Article.visible.filter(tags__in=[tag]).count()
    return count

@register.simple_tag
def get_personal_info():
    return InformationSetup.objects.first()

@register.simple_tag
def get_social_media_links():
    return SocialMediaLink.objects.all()