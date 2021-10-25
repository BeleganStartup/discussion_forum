# Django
from django.contrib import admin
# Forum
from forum.models import Post, Like


# Register models
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
