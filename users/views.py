from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View


# Create your views here.
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
