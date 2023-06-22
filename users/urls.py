from django.urls import path
from .views import RegistrationView, profile
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("login", LoginView.as_view(template_name="users/login.html"), name="login"),
    path(
        "logout", LogoutView.as_view(template_name="users/logout.html"), name="logout"
    ),
    path("register", RegistrationView.as_view(), name="register"),
    path("<str:username>", profile, name="profile"),
]