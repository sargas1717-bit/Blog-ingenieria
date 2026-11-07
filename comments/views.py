from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from .models import Comment
from .forms import CommentForm
from articles.models import Article
from projects.models import Project


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/form.html"

    def get_content_object(self):
        content_type = self.kwargs.get("content_type")
        object_id = self.kwargs.get("object_id")
        model = ContentType.objects.get(model=content_type).model_class()
        return get_object_or_404(model, pk=object_id)

    def form_valid(self, form):
        content_object = self.get_content_object()
        form.instance.author = self.request.user
        form.instance.content_type = ContentType.objects.get_for_model(content_object)
        form.instance.object_id = content_object.pk
        messages.success(self.request, "Comentario agregado correctamente.")
        return super().form_valid(form)

    def get_success_url(self):
        content_object = self.get_content_object()
        if hasattr(content_object, "get_absolute_url"):
            return content_object.get_absolute_url()
        return reverse("home")


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/form.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, "Comentario actualizado correctamente.")
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.content_object.get_absolute_url()


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = "comments/confirm_delete.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.is_staff

    def get_success_url(self):
        content_object = self.object.content_object
        return content_object.get_absolute_url()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Comentario eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
