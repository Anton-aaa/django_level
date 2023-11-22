from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime

def main(request: HttpRequest):
    return render(request, 'navbar.html')

def general_information(request):
    return  HttpResponse("Information about the site.")


def create(request):
    return HttpResponse("Create new article.")

def personal_page(request, username = "asedf"):
    return render(request, 'profile.html', {"username":username})

def set_password(request):
    return HttpResponse("This is page for set password")

def set_user_data(request):
    return HttpResponse("This is page for change account information")

def deactivate(request):
    return HttpResponse("Delite account")

def register(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return HttpResponse("Way to home page")



