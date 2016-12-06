from django.conf.urls import url

from custom_messages.views import SendMessage

urlpatterns = [
    url(regex='^send_message/(?P<target_user>[-\w ]+)$',
        view=SendMessage.as_view(),
        name='send-message')
]