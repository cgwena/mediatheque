from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.models import User
from authentication.forms import LoginForm


def user_login(request):
    form = LoginForm()
    user = User.objects.all()
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is None:
                message = "Identifiants invalides"
            else:
                login(request, user)
                if user.is_staff:
                    return redirect("home")
                else:
                    return redirect("users_home")
    return render(
        request, "authentication/login.html", {"form": form, "message": message}
    )


def logout_user(request):
    logout(request)
    return redirect("login")
