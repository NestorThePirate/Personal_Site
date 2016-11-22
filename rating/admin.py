from django.contrib import admin
from .models import RatingModel


class RatingModelExpand(admin.ModelAdmin):
    list_display = ('__str__', 'score', 'likes', 'dislikes', 'created', 'edited')


admin.site.register(RatingModel, RatingModelExpand)
