from django.contrib import admin
from .models import (Article,
                     Topic,
                     Comment)
import datetime

class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'publications', 'author')
    list_display = ( 'title', 'id', 'text', 'created_at', 'updated_at', 'author')


admin.site.register(Article, ArticleAdmin)

class TopicAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'prefers')
    list_display = ('title', 'description')

admin.site.register(Topic, TopicAdmin)

class CommentAdmin(admin.ModelAdmin):
    fields = ('message', 'contains', 'author')
    list_display = ('message', 'created_at', 'contains', 'author')

admin.site.register(Comment, CommentAdmin)

