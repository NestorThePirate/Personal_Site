from article.models import Article
from .models import RatingModel
from comment.models import CommentModel
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Article)
@receiver(post_save, sender=CommentModel)
def rating_model_save(sender, instance, **kwargs):
    if len(instance.rating_object.all()) < 1:
        RatingModel.objects.create(content_object=instance)
