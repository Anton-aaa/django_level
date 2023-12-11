from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from myapp.models import Topic, Article


def topics(request):
    all_topics = Topic.objects.all()
    return render(request, 'topics.html', {"topics": all_topics})

def get_topic(request, topic_id):
    topic = Topic.objects.filter(id=topic_id).first()
    articles = Article.objects.filter(publications=topic)
    return render(request, 'topic_details.html', {"details": topic, "articles": articles})


def topic_subscribe(request, topic_subject):
    return HttpResponse("Thanks for subscribing, best human)")

def topic_unsubscribe(request, topic_subject):
    return HttpResponse("No, please, stay(")