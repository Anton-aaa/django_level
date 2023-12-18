from .views import (topics, topic_subscribe, topic_unsubscribe, TopicList, get_topic)
from django.urls import path,include

urlpatterns = [
    path("", TopicList.as_view(), name="topics"),
    path("<int:pk>/", get_topic, name="topic_details_url"),
    path("<slug:topic_subject>/subscribe", topic_subscribe),
    path("<slug:topic_subject>/unsubscribe", topic_unsubscribe),
]
