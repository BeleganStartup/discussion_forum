# Django
from rest_framework import serializers
# Forum
from forum.models import Post, Like


class PostListSerializer(serializers.ModelSerializer):
    num_of_likes = serializers.SerializerMethodField()

    def get_num_of_likes(self, obj):
        """ Calculate number of likes for each post """
        likes_instance = obj.get_likes(Like)
        count_likes = obj.count_likes(likes_instance)
        return count_likes

    class Meta:
        model = Post
        fields = ('slug', 'title', 'create_date', 'num_of_likes')
