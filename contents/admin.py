from django.contrib import admin

# Register your models here.
from .models import UserPost,UserPostMedia,UserProfile,PostComment,PostLikes


class UserPostAdmin(admin.ModelAdmin):
    list_display =('caption_text','is_published','author',)

class PostCommentAdmin(admin.ModelAdmin):
    list_display =('text','post','author',)


admin.site.register(UserProfile)
admin.site.register(UserPost,UserPostAdmin)
admin.site.register(UserPostMedia)
admin.site.register(PostComment,PostCommentAdmin)
admin.site.register(PostLikes)