from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpRequest


def fetchPosts(request):
    response = "These are the posts that have been fetched"

    return HttpResponse(response)


def fetchPosts_with_name(request: HttpRequest, name):
    print(request.headers)
    print(request.content_params)
    return HttpResponse("Hello %s, I will fetch posts for you." % name)
