from .views import comment, update, delete, ArticleDetailView
from django.urls import path


urlpatterns = [

    path("", ArticleDetailView.as_view(), name='article_url'),
    path("comment/", comment),
    path("update/", update),
    path("delete/", delete),
]