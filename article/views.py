from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import JsonResponse, Http404
from django.db.models import Q
from django.views import generic
from comment.models import CommentModel
from tag.models import Tag
from .models import Article, Subscription
from .forms import ArticleForm
from tag.forms import TagFormSet
from comment.forms import CommentForm
from hitcount.views import HitCountMixIn
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


class CreateArticle(generic.FormView):
    form_class = ArticleForm
    template_name = 'article/add_article.html'
    article = None

    def get_success_url(self):
        return reverse('article-details', args=[self.article.primary_key])

    def form_valid(self, form):
        self.article = Article.objects.create(user=self.request.user,
                                              title=form.cleaned_data.get('title'),
                                              text=form.cleaned_data.get('text'))
        self.article.save()
        new_tag = Tag.objects.create(tag=form.cleaned_data.get('tag'),
                                     user=self.request.user)
        new_tag.save()
        new_tag.article.add(self.article)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user is None:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class UpdateArticle(generic.FormView):
    form_class = ArticleForm
    template_name = 'article/add_article.html'
    article = None
    tag = None

    def get_success_url(self):
        return reverse('article-details', args=[self.article.primary_key])

    def get_initial(self):
        initial = super().get_initial()
        initial['title'] = self.article.title
        initial['text'] = self.article.text
        initial['tag'] = self.tag
        return initial

    def form_valid(self, form):
        self.article.save()
        self.tag.save()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        self.article = Article.objects.get(primary_key=kwargs['article_pk'])
        self.tag = Tag.objects.get(article=self.article)
        return super().dispatch(request, *args, **kwargs)


class ArticleDetails(HitCountMixIn, generic.FormView):
    form_class = CommentForm
    article = None
    template_name = 'article/article_details.html'

    def get_success_url(self):
        return reverse('article-details', args=[str(self.article.primary_key)])

    def get_context_data(self, **kwargs):
        ctx = super(ArticleDetails, self).get_context_data(**kwargs)
        ctx['article'] = self.article
        ctx['comments'] = self.article.get_comment_list()
        return ctx

    def dispatch(self, request, *args, **kwargs):
        self.article = get_object_or_404(Article, pk=kwargs['article_pk'])
        self.add_hit(request, self.article.get_hit_counter())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.user = self.request.user
        parent_pk = form['parent'].value()
        if parent_pk is not '':
            new_comment.parent = CommentModel.objects.get(pk=parent_pk)
        new_comment.article = self.article
        new_comment.save()
        return super().form_valid(form)


class SubscriptionManagement(generic.RedirectView):
    article = None
    user = None

    def get_redirect_url(self, *args, **kwargs):
        return reverse('article-details', args=[self.article.primary_key])

    def dispatch(self, request, *args, **kwargs):
        self.article = get_object_or_404(Article, primary_key=kwargs['primary_key'])
        self.user = request.user
        if self.user is None:
            return self.get_redirect_url(*args, **kwargs)

        try:
            subscription = Subscription.objects.get(article=self.article,
                                                    subscribed_user=self.user
                                                    )
            subscription.delete()

        except ObjectDoesNotExist:
            subscription = Subscription.objects.create(article=self.article,
                                                       subscribed_user=self.user
                                                       )
            subscription.save()
        return super().dispatch(request, *args, **kwargs)
