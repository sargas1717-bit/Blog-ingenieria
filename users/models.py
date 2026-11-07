from django.contrib.auth.models import AbstractUser
from django.db import models


class EngineeringBranch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Rama de Ingeniería"
        verbose_name_plural = "Ramás de Ingeniería"

    def __str__(self):
        return self.name


class User(AbstractUser):
    profession = models.CharField(max_length=100, blank=True)
    engineering_branch = models.ForeignKey(
        EngineeringBranch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username
