from django.conf.urls import url
from . import views


urlpatterns = [
    url(regex='^$',
        view=views.MainPage.as_view(),
        name='article-list'),

    url(regex='^add_article/$',
        view=views.CreateArticle.as_view(),
        name='add-article'),

    url(regex='^article/(?P<article_pk>[-\w]+)$',
        view=views.ArticleDetails.as_view(),
        name='article-details'),

    url(regex='^article/edit/(?P<article_pk>[-\w]+)$',
        view=views.UpdateArticle.as_view(),
        name='update-article'),

    url(regex='^filter/tag/(?P<tag>[-\w ]+)/$',
        view=views.MainPage.as_view(),
        name='article-list'),
    ]
