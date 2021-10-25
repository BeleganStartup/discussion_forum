# DRF
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Forum
from forum.models import Post
from forum.serializers import PostListSerializer, PostDetailSerializer


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

    def post(self, request):
        # Create Post
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Extract data
            title = serializer.data.get("title")
            content = serializer.data.get("content")
            # Return Post
            post = Post.objects.create(
                owner = request.user,
                title = title,
                content = content,
            )
            resp = {
                "details": {
                    "message": "Post has been created",
                    "url": post.get_absolute_url()
                }
            }
            return Response(resp, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPI(APIView):
    """ Create, Retreive, Update, and Delete a Post """
    serializer_class = PostDetailSerializer

    def get(self, request, slug):
        # Retreive Post
        try:
            query = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return Response({"details": "Post is not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.serializer_class(instance=query)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, slug):
        # Delete Post
        try:
            post = Post.objects.get(slug=slug, owner=request.user)
        except Post.DoesNotExist:
            return Response({"details": "Post is not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            post.delete()
            return Response({"details": "Post has been deleted."}, status=status.HTTP_200_OK)

    def patch(self, request, slug):
        # Update Post
        try:
            post = Post.objects.get(slug=slug, owner=request.user)
        except Post.DoesNotExist:
            return Response({"details": "Post is not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.serializer_class(post, data=request.data, partial=True)
            if serializer.is_valid():
                print(serializer.validated_data)
                serializer.save()
                return Response({"details": "Post has been updated."}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
