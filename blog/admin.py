from django.contrib import admin
from . models import Category, Comment, Post, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'created', 'updated')
    list_filter = ('created', )
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','comment', 'created','updated')
    list_filter = ('user','comment', 'created','updated')
    search_fields = ('user','comment')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)