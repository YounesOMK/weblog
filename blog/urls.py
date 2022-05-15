from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('articles/<int:year>/<int:month>/<int:day>/<slug:article>/', views.ArticleDetailView.as_view(), name='article_detail'),
    #path('filter/', views.ArticleFilterView.as_view(), name='article_filter'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tagged/<slug:tag_slug>/', views.HomeView.as_view(), name='article_list_by_tag'),
]


htmx_urlpatterns = [
    path('articles/<int:pk>/comments/', views.comment_list, name='comment_list'),
]

urlpatterns += htmx_urlpatterns