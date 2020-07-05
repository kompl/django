from django.shortcuts import redirect
from django.views.generic import ListView
from blog.models import Post
from services.search import SearchResult


def redirect_blog(request):
    return redirect('posts_list_url', permanent=True)
