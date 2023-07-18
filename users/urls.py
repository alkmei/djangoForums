from django.urls import path, include
from .views import RegistrationView, profile
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("accounts/register", RegistrationView.as_view(), name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("users/<str:username>", profile, name="profile"),
]
