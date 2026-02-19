from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "likes",
        "created_at",
        "body"
    )

admin.site.register(Post,PostAdmin)

