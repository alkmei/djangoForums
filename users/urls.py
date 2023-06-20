from django.urls import path
from .views import CustomLoginView, RegistrationView

urlpatterns = [
    path("login", CustomLoginView.as_view(), name="login"),
    path("register", RegistrationView.as_view(), name="register"),
]
