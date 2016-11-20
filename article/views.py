from django.shortcuts import render
from django.views import generic
from comment.models import CommentModel


class MainPage(generic.ListView):
    pass