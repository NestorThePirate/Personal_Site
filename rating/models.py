from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class UserRating(models.Model):
    pass


class RatingModel(models.Model):
    score = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='tied object')
    object_id = models.SlugField()
    content_object = GenericForeignKey('content_type', 'object_id')

    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        if self.content_object == 'Article':
            obj = self.content_object.primary_key
        else:
            obj = self.content_object.pk
        return 'Rating model for: {0} ID: {1}'.format(self.content_type, obj)

    def save(self, *args, **kwargs):
        self.edited = timezone.now()
        super().save(*args, **kwargs)

    def calculate_score(self):
        self.likes = len(self.vote_set.filter(like=True))
        self.dislikes = len(self.vote_set.filter(like=False))

        self.score = self.likes - self.dislikes
        self.save()


class Vote(models.Model):
    target = models.ForeignKey(RatingModel, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)

    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True)

    def change_like(self):
        if self.like is True:
            self.like = False
        else:
            self.like = True
        self.save()
