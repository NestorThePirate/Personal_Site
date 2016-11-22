from django.shortcuts import render
from .models import Tag
from django.http import JsonResponse


def tag_autocomplete(request):
    if request.is_ajax():
        q = request.GET.get('term')
        tags = Tag.objects.filter(tag__contains=q)[:10]
        data = {'text': 'olala'}
    else:
        data ={'text': 'fail'}

    return JsonResponse(data)