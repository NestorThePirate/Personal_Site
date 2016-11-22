from django.conf.urls import url
from .views import tag_autocomplete

urlpatterns = [
    url(regex='^/tag/tag_autocomplete/$',
        view=tag_autocomplete,
        name='tag-autocomplete')
]
