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
from myapp.views import form_view
from django.contrib import admin
from django.urls import path, include
from myapp.views import (main,
                         general_information,
                         create,
                         personal_page,
                         set_password,
                         set_user_data,
                         deactivate,
                         register,
                         my_login,
                         my_logout,
                         search_article,
                         add_comment,
                         )


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main, name='main'),
    path("about", general_information, name="about"),
    path("article/<int:article_id>/", include("myapp.article.urls_article")),
    path("create_article", create, name='create_article'),
    path("topics/", include("myapp.topics.urls_topics")),
    path("profile/<str:username>/", personal_page, name="personal_page"),
    path("set-password/", set_password),
    path("set-userdata/", set_user_data),
    path("deactivate/", deactivate),
    path("register/", register, name="register"),
    path("login/", my_login, name="login"),
    path("logout/", my_logout, name="logout"),
    path('search', search_article, name='search'),
    path("add_comment/<int:article_id>", add_comment, name='add_comment')
]
