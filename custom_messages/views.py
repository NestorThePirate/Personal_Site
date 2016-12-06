from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import Http404
from django.views import generic

from custom_messages.forms import MessageForm
from custom_messages.models import PrivateMessage


class SendMessage(generic.FormView):
    template_name = 'messages/send_message.html'
    form_class = MessageForm
    target_user = None

    def form_valid(self, form):
        new_message = PrivateMessage.objects.create(author_user=self.request.user,
                                                    title=form.cleaned_data.get('title'),
                                                    text=form.cleaned_data.get('text'))
        if self.target_user:
            new_message.target_user = self.target_user
        else:
            new_message.target_user = form.cleaned_data.get('target_user')
        new_message.save()
        return self.form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        try:
            self.target_user = kwargs['user-slug']
        except ObjectDoesNotExist:
            pass
        if self.request.user is None:
            raise Http404
        return super().dispatch(request, *args, **kwargs)
