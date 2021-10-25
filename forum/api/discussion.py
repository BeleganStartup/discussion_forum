# DRF
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
# Forum
from forum.models import Post
from forum.serializers import PostListSerializer


class PostListAPI(APIView):
    """ List of Posts that showing limted number of posts for each page """
    pagination_class = PageNumberPagination
    serializer_class = PostListSerializer

    def get(self, request):
        # Retreive Posts
        query = Post.objects.order_by('create_date')
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset=query, request=request)
        serializer = self.serializer_class(instance=result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
