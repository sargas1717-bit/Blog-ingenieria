"""
URL configuration for blog_core project.
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("users.urls")),
    path("articulos/", include("articles.urls")),
    path("proyectos/", include("projects.urls")),
    path("comentarios/", include("comments.urls")),
]
