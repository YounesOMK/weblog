from django.contrib import admin

from .models import InformationSetup, Article, Project, SocialMediaLink, Comment

@admin.register(InformationSetup)
class InformationSetupAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone_number',
        'cv_file'
    )

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status',)
    list_filter = ('status', 'created', 'publish',)
    search_fields = ('title', 'body',)

    prepopulated_fields = {
        'slug': ('title',)
    }

    date_hierarchy = 'publish'

    ordering = ('status', 'publish')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status', 'link')
    list_filter = ('status', 'created', 'publish',)

    prepopulated_fields = {
        'slug': ('title',)
    }

    date_hierarchy = 'publish'

    ordering = ('status', 'publish')


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class', 'url')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner_pseudo_name',)
    list_filter = ('status',)

    date_hierarchy = 'publish'

    ordering = ('status', 'publish')

