from django import forms
from media.models import Livre, Dvd, Cd, JeuDePlateau


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


