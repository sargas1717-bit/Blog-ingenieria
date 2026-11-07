from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, EngineeringBranch


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Información adicional", {"fields": ("profession", "engineering_branch", "created_at")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Información adicional", {"fields": ("profession", "engineering_branch")}),
    )
    list_display = ("username", "email", "profession", "engineering_branch", "is_staff")
    list_filter = ("engineering_branch", "is_staff", "is_superuser")


@admin.register(EngineeringBranch)
class EngineeringBranchAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
