from django import forms
from .models import CommentModel
from django.utils import timezone


class CommentForm(forms.ModelForm):
    parent = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'parent'}), required=False)

    class Meta:
        model = CommentModel
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean_text(self):
        text = self.cleaned_data.get('text')
        try:
            time_block = timezone.now().minute - self.user.get_last_comment_created().minute
            print(time_block)
            if time_block < 1:
                raise forms.ValidationError('Вы оставляете сообщения слишком быстро')
        except AttributeError:
            pass

        return text
