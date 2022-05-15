from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import View
from django.views.generic.list import MultipleObjectMixin


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from taggit.models import Tag

# Local models

from .models import InformationSetup, SocialMediaLink, Article, Comment

# Local forms

from .forms import CommentForm

# Filters

class HomeView(TemplateResponseMixin, View):
    template_name = 'home.html'
    tag = None
    articles = None


    def dispatch(self, request, tag_slug=None):
        self.articles = Article.visible.all()

        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            self.articles = self.articles.filter(tags__in=[tag])

        return super().dispatch(request, tag_slug)


    def get(self, request, *args, **kwargs):

        # information = InformationSetup.objects.first()
        # social_media_links = SocialMediaLink.objects.all()

        # Pagination

        paginator = Paginator(self.articles, 10)
        page = request.GET.get('page')

        try:
            self.articles = paginator.page(page)

        except PageNotAnInteger:
            self.articles = paginator.page(1)

        except EmptyPage:
            self.articles = paginator.page(paginator.num_pages)

        if request.META.get('HTTP_HX_REQUEST'):
            self.template_name = 'includes/article_list.html'
            
        return self.render_to_response({
            # 'information': information,
            # 'social_media_links': social_media_links,
            'articles': self.articles,
        })

class ArticleDetailView(TemplateResponseMixin, View):
    
    template_name = 'article_detail.html'
    article = None


    def dispatch(self, request, article, year, month, day):
        self.article = get_object_or_404(Article, slug=article, status='visible', publish__year=year, publish__month=month, publish__day=day)

        return super().dispatch(request, article, year, month, day)

    def get(self, request, *args, **kwargs):

        comments = self.article.comments.filter(status='visible')

        form = CommentForm()

        return self.render_to_response({
            'article': self.article,
            'form': form,
            'comments': comments
        })

    def post(self, request, *args, **kawrgs):
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.article = self.article
            form.save()

            # Html comment
            return HttpResponse(f"""
                <div id="comment_{form.id}" class="comment bg-white smooth shadow-sm rounded my-2 p-2" >
                    <span class="h4 fw-lighter border-bottom " >{form.owner_pseudo_name}</span>
                    <p class="lead text-muted my-2" >
                        { form.comment }
                    </p>
                </div>
            """)

        else:
            return HttpResponse(f"""
                <div class="alert alert-danger" >
                    something is wrong
                </div>
            """)
        return self.render_to_response({
            'form': form
        })

 
# For htmx
def comment_list(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'includes/partials/comment_list.html', {
        'comments': article.comments.all()
    })



class TagListView(TemplateResponseMixin, View):

    template_name = 'tag_list.html'

    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        # information = InformationSetup.objects.first()
        # social_media_links = SocialMediaLink.objects.all()

        return self.render_to_response({
            'tags': tags,
            # 'information': information,
            # 'social_media_links': social_media_links,
        })