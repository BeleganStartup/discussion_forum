# Django
from django.urls import path
# Forum
from forum.api.discussion import PostListAPI


urlpatterns = [
    path('post/', PostListAPI.as_view(), name="posts_list")
]
