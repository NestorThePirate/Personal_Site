from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import generic
from comment.models import CommentModel
from tag.models import Tag
from .models import Article
from .forms import ArticleForm
from tag.forms import TagFormSet
from django.core.exceptions import ObjectDoesNotExist


class MainPage(generic.ListView):
    template_name = 'article/article_list.html'
    search_list = Article.objects.all()
    paginate_by = 10

    def get_queryset(self):
        return self.search_list

    def dispatch(self, request, *args, **kwargs):
        if 'q' in request.GET:
            self.search_list = Article.objects.filter(Q(title__contains=request.GET['q']) |
                                                      Q(text__contains=request.GET['q'])
                                                      )
        return super().dispatch(request, *args, **kwargs)


class ArticleDetails(generic.FormView):
    pass


class CreateArticle(generic.View):
    article_form = ArticleForm
    tag_forms = TagFormSet

    def post(self, request):
        new_article = None

        self.article_form = ArticleForm(request.POST)
        self.tag_forms = TagFormSet(request.POST)

        if self.article_form.is_valid():
            new_article = self.article_form.save(commit=False)
            new_article.user = request.user

        if self.tag_forms.is_valid() and new_article:
            new_article.save()
            for form in self.tag_forms:
                try:
                    ex_tag = Tag.objects.get(tag=form.cleaned_data.get('tag'))
                    ex_tag.article.add(new_article)
                except ObjectDoesNotExist:
                    new_tag = form.save(commit=False)
                    new_tag.user = request.user
                    new_tag.save()
                    new_tag.article.add(new_article)

                return redirect('article-details', pk=new_article.pk)
        return self.get(request)

    def get(self, request):
        return render(request, 'article/add_article.html', {'article_form': self.article_form,
                                                            'tag_forms': self.tag_forms
                                                            })
