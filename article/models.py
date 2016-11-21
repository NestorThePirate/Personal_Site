from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from rating.models import RatingModel
from django.conf import settings


class ArticleManager(models.Manager):
    def high_rated_articles(self):
        return super(ArticleManager, self).get_queryset().filter()


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True)

    rating_object = GenericRelation(RatingModel)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def save(self, *args, **kwargs):
        self.edited = timezone.now()
        super().save(*args, **kwargs)

    objects = ArticleManager

    def get_article_rating_model(self):
        return self.rating_object.last()

    def get_article_score(self):
        return self.rating_object.last().score

    def get_comment_list(self):
        return self.commentmodel_set.all()

    def get_number_of_comments(self):
        return len(self.commentmodel_set.all())
