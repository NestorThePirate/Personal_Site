from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from rating.models import RatingModel
from hitcount.models import HitCount
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
    hit_count_object = GenericRelation(HitCount)

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

    def get_likes(self):
        return self.rating_object.last().vote_set.filter(like=True).count()

    def get_dislikes(self):
        return self.rating_object.last().vote_set.filter(like=False).count()

    def get_comment_list(self):
        return self.commentmodel_set.all()

    def get_number_of_comments(self):
        return len(self.commentmodel_set.all())

    def get_hit_counter(self):
        return self.hit_count_object.last()

    def get_hits(self):
        return self.hit_count_object.last().hit_set.all().count()
