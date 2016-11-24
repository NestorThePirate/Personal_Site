from django import forms
from . import models
from user.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            CustomUser.objects.get(username=username)
        except ObjectDoesNotExist:
            raise forms.ValidationError("The user doesn't exist or is not activated")
        return username



