from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User


class RegistrationView(View):
    form_class = UserCreationForm
    template_name = "users/register.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, self.template_name, {"form": form})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(Profile, user=user)
    context = {"profile": user_profile}
    return render(request, "users/profile.html", context)
