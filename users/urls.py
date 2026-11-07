from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("<str:username>/", views.ProfileView.as_view(), name="profile"),
    path("ramas/", views.BranchListView.as_view(), name="branch_list"),
    path("ramas/<slug:slug>/", views.BranchDetailView.as_view(), name="branch_detail"),
]
