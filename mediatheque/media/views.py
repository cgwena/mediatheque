from django.shortcuts import render, redirect
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)

from media.models import Livre, Dvd, Cd, JeuDePlateau, Media
from users.models import User
from media.forms import (
    LivreForm,
    DvdForm,
    CdForm,
    JeuForm,
)


def is_staff_user(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_staff_user)
def home(request):
    return render(request, "media/home.html")


@login_required
@user_passes_test(is_staff_user)
def media(request):
    livres = Livre.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(
        request,
        "media/media.html",
        {"livres": livres, "dvds": dvds, "cds": cds, "jeux": jeux},
    )


@login_required
@user_passes_test(is_staff_user)
def media_detail(request, id):
    media = Media.objects.get(id=id)
    return render(request, "media/media_detail.html", {"media": media})



@login_required
@user_passes_test(is_staff_user)
def jeu_detail(request, id):
    jeu = JeuDePlateau.objects.get(id=id)
    return render(request, "media/jeu_detail.html", {"jeu": jeu})


@login_required
@user_passes_test(is_staff_user)
def livre_create(request):
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            livre = form.save()
            return redirect("media_detail", livre.id)
    else:
        form = LivreForm()
    return render(request, "media/livre_create.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def dvd_create(request):
    if request.method == "POST":
        form = DvdForm(request.POST)
        if form.is_valid():
            dvd = form.save()
            return redirect("media_detail", dvd.id)
    else:
        form = DvdForm()
    return render(request, "media/dvd_create.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def cd_create(request):
    if request.method == "POST":
        form = CdForm(request.POST)
        if form.is_valid():
            cd = form.save()
            return redirect("media_detail", cd.id)
    else:
        form = CdForm()
    return render(request, "media/cd_create.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def jeu_create(request):
    if request.method == "POST":
        form = JeuForm(request.POST)
        if form.is_valid():
            jeu = form.save()
            return redirect("jeu_detail", jeu.id)
    else:
        form = JeuForm()
    return render(request, "media/jeu_create.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def media_update(request, id):
    livre = Livre.objects.get(id=id)
    if request.method == "POST":
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect("media_detail", media.id)
    else:
        form = LivreForm(instance=livre)
    return render(request, "media/media_update.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def dvd_update(request, id):
    dvd = Dvd.objects.get(id=id)
    if request.method == "POST":
        form = DvdForm(request.POST, instance=dvd)
        if form.is_valid():
            form.save()
            return redirect("media_detail", dvd.id)
    else:
        form = DvdForm(instance=dvd)
    return render(request, "media/media_update.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def cd_update(request, id):
    cd = Cd.objects.get(id=id)
    if request.method == "POST":
        form = CdForm(request.POST, instance=cd)
        if form.is_valid():
            form.save()
            return redirect("media_detail", cd.id)
    else:
        form = CdForm(instance=cd)
    return render(request, "media/media_update.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def jeu_update(request, id):
    jeu = JeuDePlateau.objects.get(id=id)
    if request.method == "POST":
        form = JeuForm(request.POST, instance=jeu)
        if form.is_valid():
            form.save()
            return redirect("jeu_detail", jeu.id)
    else:
        form = JeuForm(instance=jeu)
    return render(request, "media/media_update.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def media_delete(request, id):
    media = Media.objects.get(id=id)
    if request.method == "POST":
        media.delete()
        return redirect("media")
    return render(request, "media/media_delete.html", {"media": media})

@login_required
@user_passes_test(is_staff_user)
def jeu_delete(request, id):
    jeu = JeuDePlateau.objects.get(id=id)
    if request.method == "POST":
        jeu.delete()
        return redirect("media")
    return render(request, "media/media_delete.html", {"media": jeu})