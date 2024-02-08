from django.shortcuts import render, redirect
from bibliothecaire.models import Livre, Dvd, Cd, JeuDePlateau
from users.models import User
from users.forms import UserForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_staff_user(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_staff_user)
def users(request):
    user = User.objects.all()
    return render(request, "users/users.html", {"user": user})


@login_required
@user_passes_test(is_staff_user)
def user_detail(request, id):
    user = User.objects.get(id=id)
    return render(request, "users/user_detail.html", {"user": user})


@login_required
@user_passes_test(is_staff_user)
def user_create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
    else:
        form = UserForm()
    return render(request, "users/user_create.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def user_update(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_detail", user.id)
    else:
        form = UserForm(instance=user)
    return render(request, "users/user_update.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def user_delete(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        return redirect("users")
    return render(request, "users/user_delete.html", {"user": user})


@login_required
def home(request):
    livres = Livre.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(
        request,
        "users/home.html",
        {"livres": livres, "dvds": dvds, "cds": cds, "jeux": jeux},
    )
