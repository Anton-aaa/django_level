from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def get_article(request, article_id):
    return   HttpResponse(f"Information about the article {article_id}.")

def comment(request, article_id):
    return HttpResponse("Create new comment.")

def update(request,article_id):
    return HttpResponse("Update article.")

def delete(request,article_id):
    return HttpResponse("Delete.")
