from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import DetailView

from myapp.forms import CommentForm
from myapp.models import Article, Comment


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


# def get_article(request, article_id):
#     arti = Article.objects.filter(id=article_id).first()
#     comm = Comment.objects.filter(contains=arti)
#     return render(request, 'article_details.html', {"details": arti, "comments": comm})

def comment(request, article_id):
    return HttpResponse("Create new comment.")

def update(request,article_id):
    return HttpResponse("Update article.")

def delete(request,article_id):
    return HttpResponse("Delete.")
