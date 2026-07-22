from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created!")
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "users/login.html"