from django.urls import path
from .views import RegistrationView, profile
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register", RegistrationView.as_view(), name="register"),
    path("<str:username>", profile, name="profile"),
]
