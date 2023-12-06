from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render
from myapp.forms import AuthenticationForm, RegisterForm
from django.contrib.auth import login
from django.urls import reverse

from myapp.forms import MyForm
from myapp.models import Article


def main(request):
    all_article = Article.objects.all()
    return render(request, 'main.html', {"articles": all_article})

def general_information(request):
    return  HttpResponse("Information about the site.")

def create(request):
    return HttpResponse("Create new article.")

def personal_page(request, username = "asedf"):
    return render(request, 'profile.html', {"username": username})

def set_password(request):
    return HttpResponse("This is page for set password")

def set_user_data(request):
    return HttpResponse("This is page for change account information")

def deactivate(request):
    return HttpResponse("Delite account")

def register(request):
    if request.method == 'POST':
        form = RegisterForm.clean(request.POST)
        if form.is_valid():
            User.objects.create_user(username= form.username, password= form.password)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    return render(request, 'form_registration.html', {'form': form})

def my_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect(reverse("form-view"))
        else:
            return render(request, "login.html", {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    return HttpResponse("Way to home page")

def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            User.objects.create_user(form)
            return HttpResponseRedirect('/')
    else:
        form = MyForm()

    return render(request, 'form.html', {'form': form})



