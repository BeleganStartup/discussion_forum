# Django
from django.contrib import admin
# Forum
from forum.models import Post, Like


# Register models
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    filter_horizontal = ('user', )
    readonly_fields = ('post', )

    def has_add_permission(self, *args, **kwargs):
        return False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'last_update_date', )
    readonly_fields = ('slug', 'create_date', 'last_update_date', )
