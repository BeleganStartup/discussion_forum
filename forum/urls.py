# Django
from django.urls import path
# Forum
from forum.api.discussion import PostListAPI, PostDetailAPI


urlpatterns = [
    path('post/', PostListAPI.as_view(), name="post_list"),
    path('post/<slug:slug>/', PostDetailAPI.as_view(), name="post_detail")
]
