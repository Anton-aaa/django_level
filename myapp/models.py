from django.db import models
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_article', null=True, blank=True)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    publications = models.ManyToManyField(Article)
    prefers = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    contains = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='contains', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment', null=True, blank=True)

    def __str__(self):
        return self.message



