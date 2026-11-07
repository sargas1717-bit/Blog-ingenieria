from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "w-full border border-gray-300 p-2 rounded",
                "rows": 4,
                "placeholder": "Escribe tu comentario...",
            }),
        }
