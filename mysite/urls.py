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
                         LogoutSuccessView,
                         ArticleDeleteView,
                         CommentDeleteView,
                         ArticleUpdateView,
                         MyPasswordResetDoneView,
                         SettingView,
                         ExactlyDelView,
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
    path('deactivate/exactly_del/', ExactlyDelView.as_view(), name='exactly_del'),
    path("deactivate/<int:pk>/", ProfileDeleteView.as_view(), name="deactivate"),
    path("register/", Register.as_view(), name="register"),
    path("login/", MyLogin.as_view(), name="login"),
    path("logout/", MyLogout.as_view(), name="logout"),
    path("logout_success/", LogoutSuccessView.as_view(), name='logout_success'),
    path('search', search_article, name='search'),
    path("add_comment/<int:pk>/", CreateComment.as_view(), name='add_comment'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('settings/', SettingView.as_view(), name='settings'),
]
