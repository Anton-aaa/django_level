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
                         personal_page,
                         set_password,
                         set_user_data,
                         deactivate,
                         Register,
                         MyLogin,
                         MyLogout,
                         search_article,
                         CreateComment,
                         no_logout,
                         ArticleDeleteView,
                         CommentDeleteView,
                         ArticleUpdateView
                         )


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ArticleListView.as_view(), name='main'),
    path("about", AboutView.as_view(), name="about"),
    path("article/<int:pk>/", include("myapp.article.urls_article")),
    path("create_article", CreateArticle.as_view(), name='create_article'),
    path("topics/", include("myapp.topics.urls_topics")),
    path("profile/<int:username>/", personal_page, name="personal_page"),
    path("set-password/", set_password),
    path("set-userdata/", set_user_data),
    path("deactivate/", deactivate),
    path("register/", Register.as_view(), name="register"),
    path("login/", MyLogin.as_view(), name="login"),
    path("logout/", MyLogout.as_view(), name="logout"),
    path('search', search_article, name='search'),
    path("add_comment/<int:pk>/", CreateComment.as_view(), name='add_comment'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
    path("no_logout/", no_logout, name='no_logout'),
    path("successfully/", no_logout, name='successfully'),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),

]
