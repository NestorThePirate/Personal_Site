from django.db import models
from article.models import Article
from rating.models import RatingModel
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone


class CommentModel(MPTTModel):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    text = models.TextField()
    parent = TreeForeignKey('self', blank=True, null=True)
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)

    rating_object = GenericRelation(RatingModel)

    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Comment ID: {0}'.format(self.id)

    def save(self, *args, **kwargs):
        self.edited = timezone.now()
        super().save(*args, **kwargs)

    def get_score(self):
        return self.rating_object.last().score

    get_score.short_description = "comment's score"
