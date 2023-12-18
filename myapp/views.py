from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.forms import CharField, PasswordInput, ModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, FormView, CreateView, DeleteView, ListView, UpdateView
from myapp.forms import AuthenticationForm, RegisterForm, SearchForm, ArticleForm, CommentForm, UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from myapp.models import Article, Comment


class ArticleListView(ListView):
    model = Article
    template_name = 'main.html'
    context_object_name = "articles"


class AboutView(TemplateView):
    template_name = "about.html"


class CreateArticle(LoginRequiredMixin, CreateView):
    template_name = "create_article.html"
    model = Article
    fields = ['title', 'text', 'publications']
    success_url = reverse_lazy('main')
    login_url = '/login/'

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


def personal_page(request, username = "asedf"):
    return render(request, 'profile.html', {"username": username})

def set_password(request):
    return HttpResponseRedirect(reverse('article_url', args=[46]))

def set_user_data(request):
    return HttpResponse("This is page for change account information")

def deactivate(request):
    return HttpResponse("Delite account")


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'form_registration.html'
    success_url = reverse_lazy('main')


class MyLogin(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('topics')


class MyLogout(LoginRequiredMixin, LogoutView):
    login_url = '/login/'
    success_url = reverse_lazy('topics')

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        logout(request)
        redirect_to = self.get_success_url()
        if redirect_to != request.get_full_path():
            # Redirect to target page once the session has been cleared.
            return HttpResponseRedirect(reverse("main"))
        return HttpResponseRedirect(reverse("main"))


def search_article(request):
    form = SearchForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data['title']
            all_articles = Article.objects.filter(title__icontains=title)
            return render(request, 'search_result.html', {"articles": all_articles, "title":title})
    return render(request, 'search.html', {'form': form})


class CreateComment(LoginRequiredMixin, CreateView):
    login_url = 'login/'
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



def no_logout(request):
    return render(request, 'no_logout.html')


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = '/'


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = '/'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'text']
    template_name = 'article_update.html'
    success_url = '/'
    context_object_name = 'article'






