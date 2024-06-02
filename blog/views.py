from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fetchPosts(request):
    response = "These are the posts that have been fetched"

    return HttpResponse(response)