from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

from .models import Article
from .forms import ArticleForm
from comments.models import Comment
from comments.forms import CommentForm


class ArticleListView(generic.ListView):
    model = Article
    template_name = "articles/list.html"
    context_object_name = "articles"
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(status="published").select_related("author", "branch")


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = "articles/detail.html"
    context_object_name = "article"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increment_views()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content_type = ContentType.objects.get_for_model(Article)
        context["comments"] = Comment.objects.filter(
            content_type=content_type, object_id=self.object.pk
        ).select_related("author")
        context["comment_form"] = CommentForm()
        return context


class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/form.html"
    success_url = reverse_lazy("articles:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Artículo creado correctamente.")
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/form.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("articles:list")

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author or self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, "Artículo actualizado correctamente.")
        return super().form_valid(form)


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Article
    template_name = "articles/confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("articles:list")

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author or self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Artículo eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
