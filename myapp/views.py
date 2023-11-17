from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def main(request: HttpRequest):
    return HttpResponse("Main page. Blog list.")

def general_information(request):
    return  HttpResponse("Information about the site.")


def create(request):
    return HttpResponse("Create new article.")

def personal_page(request, username):
    return HttpResponse(f"This is page '{username}'.")

def set_password(request):
    return HttpResponse("This is page for change credentials")

def set_user_data(request):
    return HttpResponse("This is page for change account information")

def deactivate(request):
    return HttpResponse("Delite account")

def register(request):
    return HttpResponse("New account")

def login(request):
    return HttpResponse("Form for login")

def logout(request):
    return HttpResponse("Way to home page")
