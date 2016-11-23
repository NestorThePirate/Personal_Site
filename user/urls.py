from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex='^logout/$',
        view=views.LogoutView.as_view(),
        name='logout-view'),

    url(regex='^login/$',
        view=views.LoginView.as_view(),
        name='login-view')
]