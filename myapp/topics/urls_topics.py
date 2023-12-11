from .views import (topics, topic_subscribe, topic_unsubscribe, get_topic)
from django.urls import path,include

urlpatterns = [
    path("", topics, name="topics"),
    path("<int:topic_id>/", get_topic, name="topic_details_url"),
    path("<slug:topic_subject>/subscribe", topic_subscribe),
    path("<slug:topic_subject>/unsubscribe", topic_unsubscribe),
]
