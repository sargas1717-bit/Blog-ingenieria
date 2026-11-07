from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User, EngineeringBranch


class CustomUserCreationForm(UserCreationForm):
    profession = forms.CharField(max_length=100, required=False, label="Profesión")
    engineering_branch = forms.ModelChoiceField(
        queryset=EngineeringBranch.objects.all(),
        required=False,
        label="Rama de Ingeniería",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "profession", "engineering_branch")
