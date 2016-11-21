from django import forms
from . import models


class TagForm(forms.ModelForm):

    class Meta:
        model = models.Tag
        fields = ('tag', )

    def clean_tag(self):
        tag = self.cleaned_data.get('tag')
        if len(tag) < 5:
            raise forms.ValidationError('Тэг слишком короткий')

        return tag


class BaseTagFormSet(forms.BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        for form in self.forms:
            tag = form.cleaned_data.get('tag')
            if len(tag) <= 1:
                raise forms.ValidationError('Введите тэг')


TagFormSet = forms.formset_factory(TagForm, formset=BaseTagFormSet)
