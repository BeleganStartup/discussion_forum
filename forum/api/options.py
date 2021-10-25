# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Forum
from forum.models import Like


class LikePostAPI(APIView):
    """ Like/Unlike a post """
    def post(self, request, slug):
        try:
            post_likes = Like.objects.get(post__slug=slug)
        except Like.DoesNotExist:
            return Response({"details": "Post is not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            resp = {
                "details": {
                    "is_liked": post_likes.set_unset_like(request.user)
                }
            }
            return Response(resp, status=status.HTTP_200_OK)
