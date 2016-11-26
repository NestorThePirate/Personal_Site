from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from article.models import Subscription, Article
from comment.models import CommentModel
from tag.models import Tag


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Введите адрес электронной почты')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password
            )

        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email adress',
        max_length=255,
        unique=True
    )
    username = models.CharField(
        verbose_name='username',
        max_length=30,
        unique=True
    )
    is_active = models.BooleanField(default=False, verbose_name='activation')
    is_admin = models.BooleanField(default=False, verbose_name='Admin permission')
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='registration date')
    avatar = models.ImageField(blank=True, null=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_user_articles(self):
        return Article.objects.filter(user=self)

    def get_user_comments(self):
        return CommentModel.objects.filter(user=self)

    def get_last_comment_created(self):
        return self.get_user_comments().last().created

    def get_user_tag(self):
        return Tag.objects.filter(user=self)

    def get_user_rating(self):
        return self.userrating.rating

    def get_subscriptions(self):
        return Subscription.objects.filter(subscribed_user=self)

    def update_subscriptions(self):
        for sub in self.get_subscriptions():
            sub.get_updates()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
