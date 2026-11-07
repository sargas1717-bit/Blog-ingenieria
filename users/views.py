from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from articles.models import Article
from projects.models import Project
from .models import EngineeringBranch

from .forms import CustomUserCreationForm

User = get_user_model()


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")


class ProfileView(generic.DetailView):
    model = User
    template_name = "users/profile.html"
    context_object_name = "profile_user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.filter(author=self.object, status="published")
        context["projects"] = Project.objects.filter(author=self.object)
        return context


class BranchListView(generic.ListView):
    model = EngineeringBranch
    template_name = "users/branch_list.html"
    context_object_name = "branches"


class BranchDetailView(generic.DetailView):
    model = EngineeringBranch
    template_name = "users/branch_detail.html"
    context_object_name = "branch"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.filter(branch=self.object, status="published")
        context["projects"] = Project.objects.filter(branch=self.object)
        return context
