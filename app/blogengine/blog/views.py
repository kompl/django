from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, UpdateView
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def posts_list(request):
    posts = Post.objects.all().order_by('-date_pub')
    return render(request, 'blog/index.html', context={'posts': posts})

def tags_list(request):
    tags = Tag.objects.all().order_by('title')
    return render(request, 'blog/tags_list.html', context={'tags':tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body', 'tags', 'slug']
    template_name_suffix = '_edit_form'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts_list_url')


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class TagEdit(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['title', 'slug']
    template_name_suffix = '_edit_form'


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('tags_list_url')
