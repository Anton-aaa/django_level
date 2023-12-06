from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from myapp.models import Article, Comment


def get_article(request, article_id):
    arti = Article.objects.filter(id=article_id).first()
    comm = Comment.objects.filter(contains=arti)
    return render(request, 'article_details.html', {"details": arti, "comments": comm})

def comment(request, article_id):
    return HttpResponse("Create new comment.")

def update(request,article_id):
    return HttpResponse("Update article.")

def delete(request,article_id):
    return HttpResponse("Delete.")
