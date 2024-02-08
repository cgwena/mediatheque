from django.db import models

class Media(models.Model):
    name = models.fields.CharField(max_length=100)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
    

class Livre(Media):
    def __str__(self):
        return f"{self.name}"

    auteur = models.fields.CharField(max_length=100)


class Dvd(Media):
    def __str__(self):
        return f"{self.name}"

    realisateur = models.fields.CharField(max_length=100)


class Cd(Media):
    def __str__(self):
        return f"{self.name}"

    artiste = models.fields.CharField(max_length=100)


class JeuDePlateau(models.Model):
    def __str__(self):
        return f"{self.name}"

    name = models.fields.CharField(max_length=100)
    createur = models.fields.CharField(max_length=100, null=True)
