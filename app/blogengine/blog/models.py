from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time

def gen_slug(s):
    return f'{slugify(s, allow_unicode=True)}-{str(int(time()))}'

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length =50)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.id or self.slug == 'create':
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
