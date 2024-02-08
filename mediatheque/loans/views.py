from django.shortcuts import render, redirect
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)

from media.models import Media
from users.models import User
from loans.forms import (
    LoanForm,
)
from loans.models import Loan

import datetime


def is_staff_user(user):
    return user.is_authenticated and user.is_staff


def is_staff_user(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_staff_user)
def media_loan(request, id):
    media = Media.objects.get(id=id)
    if request.method == "POST":
        if media.disponible:

            form = LoanForm(request.POST)
            emprunt = form.save(commit=False)
            emprunt.media = media
            media.date_emprunt = emprunt.date
            user = User.objects.get(id=emprunt.emprunteur.id)

            loaned_medias = Loan.objects.all()
            dates = []
            for loaned_media in loaned_medias:
                if loaned_media.emprunteur == user:
                    date = loaned_media.date
                    dates.append(date)

            for date in dates:
                delta = datetime.date.today() - date
                if delta.days > 7:
                    return redirect("loan_late")
            if user.nombreEmprunts >= 3:
                return redirect("loan_impossible")
            else:
                media.disponible = False
                media.save()
                user.nombreEmprunts += 1
                user.save()
                emprunt.save()
            return redirect("media_detail", media.id)
        elif media.disponible == False:
            emprunt = Loan.objects.get(media=media.id)
            form = LoanForm(request.POST, instance=emprunt)
            emprunt = form.save(commit=False)
            user = User.objects.get(id=emprunt.emprunteur.id)
            media.disponible = True
            media.save()
            user.nombreEmprunts -= 1
            user.save()
            emprunt.delete()
            return redirect("media_detail", media.id)

    form = LoanForm()
    return render(request, "loans/media_loan.html", {"media": media, "form": form})


@login_required
@user_passes_test(is_staff_user)
def loan_impossible(request):
    return render(request, "loans/loan_impossible.html")


def loan_late(request):
    return render(request, "loans/loan_late.html")
