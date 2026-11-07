from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import F
from django.contrib.contenttypes.models import ContentType

from .models import Project
from .forms import ProjectForm
from comments.models import Comment
from comments.forms import CommentForm


class ProjectListView(generic.ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projects"
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.select_related("author", "branch").all()


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = "projects/detail.html"
    context_object_name = "project"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increment_views()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["user_liked"] = self.object.likes.filter(user=self.request.user).exists()
        content_type = ContentType.objects.get_for_model(Project)
        context["comments"] = Comment.objects.filter(
            content_type=content_type, object_id=self.object.pk
        ).select_related("author")
        context["comment_form"] = CommentForm()
        return context


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/form.html"
    success_url = reverse_lazy("projects:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Proyecto creado correctamente.")
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/form.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("projects:list")

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.author or self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, "Proyecto actualizado correctamente.")
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Project
    template_name = "projects/confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("projects:list")

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.author or self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Proyecto eliminado correctamente.")
        return super().delete(request, *args, **kwargs)


class ProjectLikeToggleView(LoginRequiredMixin, generic.View):
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        like, created = project.likes.get_or_create(user=request.user)
        if not created:
            like.delete()
            liked = False
        else:
            liked = True
        
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"liked": liked, "likes_count": project.likes.count()})
        
        return redirect("projects:detail", slug=project.slug)
