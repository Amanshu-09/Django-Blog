from django.urls import path
from .views import *

urlpatterns = [
    # path('', blogs.as_view(), name='blogs'),
    path('', blogs, name='blogs'),
    path('blog_detail/<int:pk>', blog_detail.as_view(), name='blog_detail'),
    path('create_blog', create_blog.as_view(), name='create_blog'),
    path('edit_blog/<int:pk>', edit_blog.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>', delete_blog.as_view(), name='delete_blog'),
    path('user_blogs', user_blogs, name='user_blogs'),
    path('like_post/<int:pk>', like_post, name='like_post'),
    path('blog_detail/<int:pk>/comment', post_comment, name='post_comment'),
    path('blog_detail/<int:pi>/comment/<int:ci>/reply', post_reply, name='post_reply'),
    path('search', search, name='search'),
    path('category/<str:cat>', category, name='category'),
]