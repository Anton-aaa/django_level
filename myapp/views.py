from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render
from myapp.forms import AuthenticationForm, RegisterForm, SearchForm, ArticleForm, CommentForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from myapp.forms import MyForm
from myapp.models import Article, Comment


def main(request):
    all_articles = Article.objects.all()
    return render(request, 'main.html', {"articles": all_articles})

def general_information(request):
    return  HttpResponse("Information about the site.")

@login_required(login_url='login/')
def create(request):
    form = ArticleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            author = request.user
            Article.objects.create(title=title, text=text, author=author)
            return render(request, 'search.html')

    return render(request, 'create_article.html', {'form': form})

def personal_page(request, username = "asedf"):
    return render(request, 'profile.html', {"username": username})

def set_password(request):
    return HttpResponse("This is page for set password")

def set_user_data(request):
    return HttpResponse("This is page for change account information")

def deactivate(request):
    return HttpResponse("Delite account")

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return render(request, 'after_registration.html')

    return render(request, 'form_registration.html', {'form': form})

def my_login(request):
    form = AuthenticationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            login(request, form.user)
            return render(request, 'after_login.html')
        else:
            return render(request, "login.html", {'form': form})
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login/')
def my_logout(request):
    logout(request)
    return HttpResponse("Logout successful")

def search_article(request):
    form = SearchForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data['title']
            all_articles = Article.objects.filter(title__icontains=title)
            return render(request, 'search_result.html', {"articles": all_articles, "title":title})
    return render(request, 'search.html', {'form': form})

@login_required(login_url='login/')
def add_comment(request, article_id):
    article = Article.objects.filter(id=article_id).first()
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            message = form.cleaned_data['message']
            Comment.objects.create(message=message, contains=article, author=request.user)
            return HttpResponseRedirect(reverse("article_url", args=(article_id,)))

    return render(request, 'create_comment.html', {'form': form, 'article': article_id})



