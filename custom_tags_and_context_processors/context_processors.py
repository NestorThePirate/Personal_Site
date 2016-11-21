from article.forms import SearchForm
from article.models import Article
from django.db.models import Count


def search_form(request):
    form = SearchForm
    return {"SEARCH_FORM": form}


def popular_articles(request):
    pass


def recent_articles(request):
    articles = Article.objects.order_by('-created')[:3]
    return {"RECENT_POSTS": articles}


def tags(request):
    pass