from django import forms
from .models import Article
from django.utils.translation import ugettext_lazy as _


class SearchForm(forms.Form):
    q = forms.CharField(
        label='',
        required=False
    )


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', ]
        labels = {'title': _('Title'),
                  'text':  _('Text')
                  }