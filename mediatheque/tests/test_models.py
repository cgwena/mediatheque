import pytest

from django.test import Client
from media.models import Book, Dvd, Cd, JeuDePlateau, Media
from users.models import User
from loans.models import Loan
from datetime import date


@pytest.mark.django_db
def test_book_model():
    client = Client()
    book = Book.objects.create(name="Les Misérables", auteur="Hugo, Victor")
    expected_value = "Les Misérables, Hugo, Victor"
    
    assert str(book) == expected_value


@pytest.mark.django_db
def test_dvd_model():
    client = Client()
    dvd = Dvd.objects.create(name="La La Land", realisateur="Chazelle, Damien")
    expected_value = "La La Land, Chazelle, Damien"

    assert str(dvd) == expected_value


@pytest.mark.django_db
def test_cd_model():
    client = Client()
    cd = Cd.objects.create(name="Homebrew", artiste="Cherry, Neneh")
    expected_value = "Homebrew, Cherry, Neneh"

    assert str(cd) == expected_value


@pytest.mark.django_db
def test_game_model():
    client = Client()
    game = JeuDePlateau.objects.create(name="Skyjo", createur="Bernhardt, Alexander")
    expected_value = "Skyjo, Bernhardt, Alexander"

    assert str(game) == expected_value


@pytest.mark.django_db
def test_user_model():
    client = Client()
    user = User.objects.create(username="JohnDoe", first_name="John", last_name="Doe", password="password123", is_staff=True)
    expected_value = "JohnDoe, Doe, John, True"

    assert str(user) == expected_value


@pytest.mark.django_db
def test_loan_model():
    user = User.objects.create(username="JohnDoe")

    media = Media.objects.create(name="Media_test")

    loan = Loan.objects.create(media=media, emprunteur=user, date=date.today())

    assert loan.media == media
    assert loan.emprunteur == user
    assert loan.date == date.today()
