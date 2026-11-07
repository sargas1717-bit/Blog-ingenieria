from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "slug", "content", "cover_image", "status", "branch"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "slug": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "content": forms.Textarea(attrs={"class": "w-full border border-gray-300 p-2 rounded", "rows": 10}),
            "status": forms.Select(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "branch": forms.Select(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
        }
