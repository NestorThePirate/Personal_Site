from django.conf.urls import url
from . import views


urlpatterns = [
    url(regex='^password_recovery/$',
        view=views.PasswordRecoveryView.as_view(),
        name='password_recovery'),

    url(regex='^password_change/$',
        view=views.PasswordChangeView.as_view(),
        name='password_change')
]
