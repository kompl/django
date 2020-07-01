from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


class SearchResult(ListView):
    model = Post
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        
        if query is not None:
            search_result_list = Post.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
        else:
            search_result_list = Post.objects.all()
        return search_result_list
