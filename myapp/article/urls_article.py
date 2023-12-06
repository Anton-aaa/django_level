from .views import get_article, comment, update, delete
from django.urls import path,include

urlpatterns = [

    path("", get_article),
    path("comment/", comment),
    path("update/", update),
    path("delete/", delete),
]