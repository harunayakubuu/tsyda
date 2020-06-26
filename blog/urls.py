from django.urls import path
from .views import (
    posts,
    post_detail,
    admin_post_list,
    admin_post_detail,
    post_create,
    post_update,
    post_delete,

    category_create,
    category_list,
    category_update,
    category_delete,

    tag_create,
    tag_list,
    tag_update,
    TagDeleteView
    # tag_delete
)

urlpatterns = [
    path('posts/', posts, name='posts'),
    path('<slug:post>/<uuid:pk>/', post_detail, name='post-detail'),

    path('post/list/', admin_post_list, name='post-list'),
    path('post/add/', post_create, name='post-create'),
    path('post/<id>/detail/', admin_post_detail, name='post-detail-admin'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),

    path('category/list/', category_list, name='category-list'),
    path('category/add/', category_create, name='category-create'),
    path('category/<id>/update/', category_update, name='category-update'),
    path('category/<id>/delete/', category_delete, name='category-delete'),

    path('tag/list/', tag_list, name='tag-list'),
    path('tag/add/',tag_create, name='tag-create'),
    path('tag/<id>/update/',tag_update, name='tag-update'),
    path('tag/<id>/delete/',TagDeleteView, name='tag-delete'),
]