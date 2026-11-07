from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "slug", "description", "content", "github_link", "demo_link", "image", "branch"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "slug": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "description": forms.Textarea(attrs={"class": "w-full border border-gray-300 p-2 rounded", "rows": 3}),
            "content": forms.Textarea(attrs={"class": "w-full border border-gray-300 p-2 rounded", "rows": 10}),
            "github_link": forms.URLInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "demo_link": forms.URLInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "branch": forms.Select(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
        }
