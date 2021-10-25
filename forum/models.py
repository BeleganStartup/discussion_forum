# Python
import uuid
# Django
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import post_save


USER = get_user_model()


# Classes
class Post(models.Model):
    owner = models.ForeignKey(USER, verbose_name="Owner", on_delete=models.CASCADE)
    slug = models.SlugField("Slug", blank=True)
    title = models.CharField("Title", max_length=128)
    content = models.TextField("Content")
    create_date = models.DateTimeField("Created at", auto_now_add=True)
    last_update_date = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        """ Display posts with "Title by Owner" structure """
        return f"{self.title} By {self.owner}"

    def get_absolute_url(self):
        """ Get Post absolute url """
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_likes(self, likes_model):
        """ Filter all likes related to current Post instance """
        likes = likes_model.objects.filter(id=self.id)
        return likes

    def count_likes(self, post_likes):
        """ There are many ways to implement a proper like counting system.
        I decided to use a method for calculating the approximate number of likes,
        which is very fast and close to acceptable. """
        # TODO: count likes
        count_post_likes = 0
        return count_post_likes


class Like(models.Model):
    post = models.ForeignKey("forum.Post", verbose_name="Post", on_delete=models.CASCADE)
    user = models.ManyToManyField(USER, verbose_name="User")
    create_like_date = models.DateTimeField("Created at", auto_now_add=True)
    last_update_date = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        """ Display posts with "Post Title" structure """
        return f"{self.post.title} Likes"

    def set_unset_like(self, target_user):
        """ When user exist then his like is counted and return True, otherwise remove it and return False"""
        try:
            self.user.objects.get(pk=target_user)
        except USER.DoesNotExist:
            self.user.add(target_user)
            like_exist = True
        else:
            self.user.remove(target_user)
            like_exist = False
        finally:
            self.user.save()
        return like_exist


# Signals
@receiver(post_save, sender=Post)
def slugify_name(sender, instance, created, **kwargs):
    """ Generate slug from title (+ random text) when post owner submit his post at first time """
    if created or instance.slug is None:
        text = slugify(instance.title)
        extra_text = str(uuid.uuid4())[0:8]
        instance.slug = f"{text}-{extra_text}"
        instance.save()