from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/edit/', PostEdit.as_view(), name='post_edit_form_url'),
    path('post/<str:slug>/delete', PostDelete.as_view(), name='post_confirm_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tags/<str:slug>/edit/', TagEdit.as_view(), name='tag_edit_form_url'),
    path('tags/<str:slug>/delete/', TagDelete.as_view(), name='tag_confirm_url')
]
