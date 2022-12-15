from django.contrib import admin
from .models import Tag, Author, Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "author")
    list_filter = ("author", "tags", "date")
    prepopulated_fields = { "slug": ("title",) }

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post", "text")

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
