from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def topics(request):
    return render(request, 'topics.html')

def topic_subscribe(request, topic_subject):
    return HttpResponse("Thanks for subscribing, best human)")

def topic_unsubscribe(request, topic_subject):
    return HttpResponse("No, please, stay(")