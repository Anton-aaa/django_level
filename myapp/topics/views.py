from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import DetailView
from django.views.generic import ListView

from myapp.models import Topic, Article


def topics(request):
    all_topics = Topic.objects.all()
    return render(request, 'topics.html', {"topics": all_topics})


# class TopicDetail(DetailView):
#     model = Topic
#     template_name = "topic_details.html"
#     context_object_name = "topic"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['article'] = Article.objects.filter(publications=context.id)
#         return context

def get_topic(request, topic_id):
    topic = Topic.objects.filter(id=topic_id).first()
    articles = Article.objects.filter(publications=topic)
    return render(request, 'topic_details.html', {"details": topic, "articles": articles})


class TopicList(ListView):
    model = Topic
    template_name = "topics.html"
    context_object_name = "topics"

def topic_subscribe(request, topic_subject):
    return HttpResponse("Thanks for subscribing, best human)")

def topic_unsubscribe(request, topic_subject):
    return HttpResponse("No, please, stay(")