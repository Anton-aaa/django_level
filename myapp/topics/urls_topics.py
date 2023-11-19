from .views import topics, topic_subscribe, topic_unsubscribe
from django.urls import path,include

urlpatterns = [
    path("", topics, name="topics"),
    path("<slug:topic_subject>/subscribe", topic_subscribe),
    path("<slug:topic_subject>/unsubscribe", topic_unsubscribe),
]
