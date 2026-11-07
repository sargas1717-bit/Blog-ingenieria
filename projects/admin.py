from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "views", "likes", "branch", "created_at")
    list_filter = ("branch", "created_at")
    search_fields = ("title", "description", "author__username")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
