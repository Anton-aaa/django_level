"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from myapp.views import (ArticleListView,
                         AboutView,
                         CreateArticle,
                         UserDetailView,
                         UserUpdatePasswordView,
                         UserUpdateView,
                         ProfileDeleteView,
                         Register,
                         MyLogin,
                         MyLogout,
                         search_article,
                         CreateComment,
                         logout_success,
                         ArticleDeleteView,
                         CommentDeleteView,
                         ArticleUpdateView,
                         MyPasswordResetDoneView,
                         settings,
                         exactly_del,
                         ArticleDetailView,
                         TopicsListView,
                         TopicDetailView,
                         SubscribeTopicView,
                         UnsubscribeTopicView
                         )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ArticleListView.as_view(), name='main'),
    path("about", AboutView.as_view(), name="about"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name='article_url'),
    path("create_article", CreateArticle.as_view(), name='create_article'),
    path("topics/", TopicsListView.as_view(), name="topic_list_url"),
    path("topics/<int:pk>/", TopicDetailView.as_view(), name="topic_details_url"),
    path("topics/", TopicsListView.as_view(), name="topic_list_url"),
    path("topics/subscribe/<int:pk>/", SubscribeTopicView.as_view(), name="topic_subscribe_url"),
    path("topics/unsubscribe/<int:pk>/", UnsubscribeTopicView.as_view(), name="topic_unsubscribe_url"),
    path("profile/<int:pk>/", UserDetailView.as_view(), name="personal_page"),
    path("set-password/", UserUpdatePasswordView.as_view(), name='set_password'),
    path("set-password/done", MyPasswordResetDoneView.as_view(), name='set_password_done'),
    path("set-userdata/", UserUpdateView.as_view(), name="set_userdata"),
    path('deactivate/exactly_del/', exactly_del, name='exactly_del'),
    path("deactivate/<int:pk>/", ProfileDeleteView.as_view(), name="deactivate"),
    path("register/", Register.as_view(), name="register"),
    path("login/", MyLogin.as_view(), name="login"),
    path("logout/", MyLogout.as_view(), name="logout"),
    path("logout_success/", logout_success, name='logout_success'),
    path('search', search_article, name='search'),
    path("add_comment/<int:pk>/", CreateComment.as_view(), name='add_comment'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('settings/', settings, name='settings'),
]
