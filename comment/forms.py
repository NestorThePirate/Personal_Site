from django import forms
from .models import CommentModel


class CommentForm(forms.ModelForm):
    parent = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'parent'}), required=False)

    class Meta:
        model = CommentModel
        fields = ('text', )

    def clean_text(self):
        text = self.cleaned_data.get('text')
        return text
