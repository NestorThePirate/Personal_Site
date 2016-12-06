from django import forms


class MessageForm(forms.Form):
    title = forms.CharField(max_length=50, label='Заголовок')
    text = forms.CharField(label='Текст')
    target_username = forms.CharField(max_length=50, label='Отправить сообщение пользователю')
