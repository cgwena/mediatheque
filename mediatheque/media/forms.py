from django import forms
from bibliothecaire.models import User, Livre, Dvd, Cd, JeuDePlateau, Emprunt


class MembreForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "is_staff", "password")


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ("name", "auteur")


class DvdForm(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = ("name", "realisateur")


class CdForm(forms.ModelForm):
    class Meta:
        model = Cd
        fields = ("name", "artiste")


class JeuForm(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = ("name", "createur")


class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ("emprunteur", "date")
