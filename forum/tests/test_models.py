# Django
from django.test import TestCase
from django.contrib.auth import get_user_model
# Forum
from forum.models import Post, Like
from forum.utils import slugify_text


USER = get_user_model()


class TestPost(TestCase):
    """ Testing Post model """

    def setUp(self):
        # Initilize post owner
        self.user = {
            "username": "normal_user",
            "password": "TestPassword",
        }
        self.owner = USER.objects.create_user(**self.user)

        # Initilize post
        self.data = {
            "title": "This is a test title",
            "content": "This is a test content",
            "owner": self.owner,
        }
        self.post = Post.objects.create(**self.data)

    def test_slug(self):
        """ Slugify the title and compare it with generated post slug """
        # Last 8 digits are random, ignore them in test
        slugified_title = slugify_text(self.post.title)[:-8]
        post_slug = self.post.slug[:-8]
        self.assertEqual(slugified_title, post_slug)

    def test_count_likes(self):
        """ Get Like instance related to Post Instance and count likes """
        likes = self.post.get_likes(Like)
        num_of_likes = self.post.count_likes(likes)
        self.assertEqual(num_of_likes, 0)


class TestLike(TestCase):
    """ Testing Like model """

    def setUp(self):
        # Initilize post owner
        self.user = {
            "username": "normal_user",
            "password": "TestPassword",
        }
        self.owner = USER.objects.create_user(**self.user)

        # Initilize post
        self.data = {
            "title": "This is a test title",
            "content": "This is a test content",
            "owner": self.owner,
        }
        self.post = Post.objects.create(**self.data)

    def test_likes_instance(self):
        """ Try getting likes instance from different ways """
        likes_instance = Like.objects.get(post=self.post)
        likes_instance_from_post = self.post.get_likes(Like)
        return self.assertEqual(likes_instance_from_post, likes_instance)

    def test_add_remove_like(self):
        """ Try owner likes his own post """
        likes_instance = self.post.get_likes(Like)
        # Like is not exist before, add it now
        likes_instance.set_unset_like(self.owner)
        # Count likes
        num_of_likes = self.post.count_likes(likes_instance)
        self.assertEqual(num_of_likes, 1)
        # Like is exist because we add it above, now delete it
        likes_instance.set_unset_like(self.owner)
        # Count likes again
        num_of_likes = self.post.count_likes(likes_instance)
        self.assertEqual(num_of_likes, 0)
