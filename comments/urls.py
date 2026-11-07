from django.urls import path

from . import views

app_name = "comments"

urlpatterns = [
    path(
        "add/<str:content_type>/<int:object_id>/",
        views.CommentCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/editar/",
        views.CommentUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/eliminar/",
        views.CommentDeleteView.as_view(),
        name="delete",
    ),
]
