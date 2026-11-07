from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="list"),
    path("nuevo/", views.ArticleCreateView.as_view(), name="create"),
    path("<slug:slug>/", views.ArticleDetailView.as_view(), name="detail"),
    path("<slug:slug>/editar/", views.ArticleUpdateView.as_view(), name="update"),
    path("<slug:slug>/eliminar/", views.ArticleDeleteView.as_view(), name="delete"),
]
