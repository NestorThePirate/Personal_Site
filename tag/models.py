from django.db import models
from article.models import Article
from django.utils import timezone
from django.db import transaction, IntegrityError
from django.conf import settings


class Tag(models.Model):
    tag = models.CharField(max_length=25)
    article = models.ManyToManyField(Article)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.tag)

    def save(self, *args, **kwargs):
        self.edited = timezone.now()
        super().save(*args, **kwargs)
