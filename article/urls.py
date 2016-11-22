from django.conf.urls import url
from . import views


urlpatterns = [
    url(regex='^$',
        view=views.MainPage.as_view(),
        name='article-list'),

    url(regex='^add_article/$',
        view=views.CreateArticle.as_view(),
        name='add-article'),

    url(regex='^article/(?P<article_id>[0-9]+)$',
        view=views.ArticleDetails.as_view(),
        name='article-details')
    ]
