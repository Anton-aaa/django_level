from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetDoneView
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.forms import CharField, PasswordInput, ModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, FormView, CreateView, DeleteView, ListView, UpdateView, DetailView
from myapp.forms import AuthenticationForm, RegisterForm, SearchForm, ArticleForm, CommentForm, UserCreationForm, \
    UserUpdateForm, UserUpdatePasswordForm
from django.contrib.auth import login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from myapp.models import Article, Comment, Topic
from django.core.cache import cache


class ArticleListView(ListView):
    model = Article
    template_name = 'main.html'
    context_object_name = "articles"
    paginate_by = 5


class AboutView(TemplateView):
    template_name = "about.html"


class CreateArticle(LoginRequiredMixin, CreateView):
    template_name = "create_article.html"
    model = Article
    fields = ['title', 'text', 'publications']
    success_url = reverse_lazy('main')
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        author = self.request.user
        article = form.save(commit=False)
        article.author = author
        article = form.save()
        return super().form_valid(form)


# class UserListView(ListView):
class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_details.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['create_form'] = CommentForm()
        context['comments'] = Comment.objects.filter(contains=kwargs['object'].id)
        return context


class UserUpdatePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = "password_update.html"
    success_url = reverse_lazy('main')
    login_url = 'login'


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "password_reset_done"


class UserUpdateView(LoginRequiredMixin, FormView):
    template_name = "username_update.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy('main')
    login_url = 'login'


    def form_valid(self, form):
        update = self.request.user
        update.username = form.cleaned_data['username']
        update.save()
        return super().form_valid(form)


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'form_registration.html'
    success_url = reverse_lazy('main')


class MyLogin(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
            return reverse('main')

class MyLogout(LoginRequiredMixin, LogoutView):
    login_url = 'login'
    def get_success_url(self):
            return reverse('main')


def search_article(request):
    form = SearchForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data['title']
            all_articles = Article.objects.filter(title__icontains=title)
            return render(request, 'search_result.html', {"articles": all_articles, "title":title})
    return render(request, 'search.html', {'form': form})


class CreateComment(LoginRequiredMixin, CreateView):
    login_url = 'login'
    http_method_names = ['post']
    form_class = CommentForm


    def form_valid(self, form):
        author = self.request.user
        new_comment = form.save(commit=False)
        new_comment.author = author
        new_comment.contains = Article.objects.get(id=self.kwargs['pk'])
        new_comment = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['contains'] = Article.objects.filter(id=self.kwargs['pk'])
        return context

    def get_success_url(self):
        if self.kwargs['pk'] is not None:
            return reverse('article_url', kwargs={'pk':self.kwargs['pk']})


class LogoutSuccessView(TemplateView):
    template_name = "logout_success.html"


class UserDetailView(DetailView):
    model = User
    template_name = "profile_details.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['topics'] = Topic.objects.filter(prefers=kwargs['object'].id)
        context['articles'] = Article.objects.filter(author=kwargs['object'].id)
        return context



class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = '/'
    login_url = 'login'


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = '/'
    login_url = 'login'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'text']
    template_name = 'article_update.html'
    success_url = '/'
    context_object_name = 'article'


class SettingView(LoginRequiredMixin, TemplateView):
    template_name = "settings.html"
    login_url = 'login'

# def settings(request):
#     return render(request, 'settings.html')


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User

    def get_success_url(self):
        return reverse('main')


class ExactlyDelView(TemplateView):
    template_name = "exactly_del.html"

class TopicsListView(ListView):
    model = Topic
    template_name = 'topics.html'
    context_object_name = "topics"
    paginate_by = 5


class TopicDetailView(DetailView):
    model = Topic
    template_name = "topic_details.html"
    context_object_name = "topic"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['article'] = Article.objects.filter(publications=kwargs['object'].id)
        return context


class SubscribeTopicView(View):
    def post(self, request, *args, **kwargs):
        topic = Topic.objects.filter(id=self.kwargs['pk']).first()
        topic.prefers.add(request.user)
        return render(request, 'subscribe_success.html', {"topic":topic})

class UnsubscribeTopicView(View):
    def post(self, request, *args, **kwargs):
        topic = Topic.objects.filter(id=self.kwargs['pk']).first()
        topic.prefers.remove(request.user)
        return render(request, 'unsubscribe_success.html')




