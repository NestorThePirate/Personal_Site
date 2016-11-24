from django.shortcuts import render
from django.views import generic
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm


class LogoutView(generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return self.request.META.get('HTTP_REFERER','/')

    def dispatch(self, request, *args, **kwargs):
        logout(self.request)
        return super().dispatch(request, *args, **kwargs)


class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password')
        )
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
