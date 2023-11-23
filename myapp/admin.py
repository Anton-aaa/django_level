from django.contrib import admin
from .models import (Article,
                     Topic,
                     Comment)
import datetime

class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'author')
    list_display = ('title', 'text', 'created_at', 'updated_at', 'author')
    #
    # def upper_name(self, obj):
    #     return obj.name.upper()

admin.site.register(Article, ArticleAdmin)

class TopicAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'publications', 'prefers')
    list_display = ('title', 'description')

admin.site.register(Topic, TopicAdmin)

class CommentAdmin(admin.ModelAdmin):
    fields = ('message', 'contains', 'author')
    list_display = ('message', 'created_at', 'contains', 'author')

admin.site.register(Comment, CommentAdmin)

