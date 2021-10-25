# Django
from rest_framework import serializers
# Forum
from forum.models import Post, Like


class PostListSerializer(serializers.ModelSerializer):
    num_of_likes = serializers.SerializerMethodField(read_only=True)

    def get_num_of_likes(self, obj):
        """ Calculate number of likes for each post """
        if not isinstance(obj, Post):
            return 0
        likes_instance = obj.get_likes(Like)
        count_likes = obj.count_likes(likes_instance)
        return count_likes

    class Meta:
        model = Post
        fields = ('slug', 'title', 'content', 'create_date', 'num_of_likes')
        write_only_fields = ('content', )
        read_only_fields = ('slug', 'create_date')


class PostDetailSerializer(serializers.ModelSerializer):
    post_owner = serializers.CharField(source='owner.username', read_only=True)
    num_of_likes = serializers.SerializerMethodField()

    def get_num_of_likes(self, obj):
        """ Calculate number of likes for each post """
        likes_instance = obj.get_likes(Like)
        count_likes = obj.count_likes(likes_instance)
        return count_likes

    class Meta:
        model = Post
        fields = ('post_owner', 'title', 'content', 'create_date', 'num_of_likes')
