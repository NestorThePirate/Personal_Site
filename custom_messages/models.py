from django.db import models
from django.conf import settings
from django.utils import timezone


class PrivateMessage(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    target_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='target')
    author_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Личное сообщение{0} от пользователя {1} пользователю {2}'.format(self.title,
                                                                                 self.author_user,
                                                                                 self.target_user
                                                                                 )
