# Django
from django.contrib import admin
# Forum
from forum.models import Post, Like


# Register models
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'last_update_date', 'num_of_likes')
    readonly_fields = ('slug', 'create_date', 'last_update_date', )

    def num_of_likes(self, obj):
        likes_instance = obj.get_likes(Like)
        counting = obj.count_likes(likes_instance)
        suffix = "Likes" if counting > 2 or counting == 0 else "Like"
        return f"{counting} {suffix}"
