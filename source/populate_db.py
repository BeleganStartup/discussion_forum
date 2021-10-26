# Python
import uuid
# Django
from django.contrib.auth import get_user_model


USER = get_user_model()


def populate_users(max_num=3600):
    """ Create bulk of users """
    USER.objects.bulk_create([USER(username=str(uuid.uuid4())[0:8], password=str(uuid.uuid4())[0:8]) for _ in range(max_num)])
    return USER.objects.all()


def add_to_likes(users, post_likes):
    """ make bulk of users likes a post """
    post_likes.user.add(*users)
