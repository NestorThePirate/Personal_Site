from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from rating.models import RatingModel


class Article(models.Model):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name='date of creation')

    rating_object = GenericRelation(RatingModel)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
