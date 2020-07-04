from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, UpdateView
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class TagEdit(UpdateView):
    model = Tag
    fields = ['title', 'slug']
    template_name_suffix = '_edit_form'


class PostEdit(UpdateView):
    model = Post
    fields = ['title', 'body', 'tags', 'slug']
    template_name_suffix = '_edit_form'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts_list_url')


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('tags_list_url')

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})
