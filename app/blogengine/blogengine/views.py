from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post
from services.search import SearchResult


def start_page(request):
    return render(request, 'start_page.html')
