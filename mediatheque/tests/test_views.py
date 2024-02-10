import pytest

from django.test import Client
from django.urls import reverse, resolve
from users.models import User
from media.models import Media, Book, Dvd, Cd, JeuDePlateau
from media.views import (
    media,
    media_detail,
    jeu_detail,
    book_create,
    dvd_create,
    cd_create,
    jeu_create,
    book_update,
    jeu_update,
    media_delete,
    jeu_delete,
)


@pytest.fixture
def staff_user():
    user = User.objects.create_user(
        username="staff_user", password="password123", is_staff=True
    )
    return user


@pytest.fixture
def non_staff_user():
    user = User.objects.create_user(
        username="non_staff_user", password="password123", is_staff=False
    )
    return user


@pytest.mark.django_db
def test_membre_add_url():
    User.objects.create(
        username="JohnDoe", first_name="John", last_name="Doe", password="password"
    )
    path = reverse("user_detail", kwargs={"id": 1})
    assert path == "/user/users/1/"
    assert resolve(path).view_name == "user_detail"


@pytest.mark.django_db
def test_user_detail_view(client, staff_user):
    client.login(username="staff_user", password="password123")
    user_to_view = User.objects.create_user(
        username="test_user", password="password123"
    )
    response = client.get(reverse("user_detail", kwargs={"id": user_to_view.id}))

    assert response.status_code == 200
    assert "user" in response.context
    assert response.context["user"] == user_to_view


@pytest.mark.django_db
def test_book_create(client, staff_user):
    client.login(username="staff_user", password="password123")
    data = {
        "name": "Test Book",
        "auteur": "Test Author",
    }

    response = client.post(reverse("book_create"), data)

    assert response.status_code == 302

    book_count = Book.objects.filter(name=data["name"], auteur=data["auteur"]).count()
    assert book_count == 1


@pytest.mark.django_db
def test_dvd_create(client, staff_user):
    client.login(username="staff_user", password="password123")
    data = {
        "name": "Test Dvd",
        "realisateur": "Test Director",
    }

    response = client.post(reverse("dvd_create"), data)

    assert response.status_code == 302

    dvd_count = Dvd.objects.filter(
        name=data["name"], realisateur=data["realisateur"]
    ).count()
    assert dvd_count == 1


@pytest.mark.django_db
def test_cd_create(client, staff_user):
    client.login(username="staff_user", password="password123")
    data = {
        "name": "Test Book",
        "artiste": "Test Artist",
    }

    response = client.post(reverse("cd_create"), data)

    assert response.status_code == 302

    cd_count = Cd.objects.filter(name=data["name"], artiste=data["artiste"]).count()
    assert cd_count == 1


@pytest.mark.django_db
def test_jeu_create(client, staff_user):
    client.login(username="staff_user", password="password123")
    data = {
        "name": "Test Book",
        "createur": "Test Creator",
    }

    response = client.post(reverse("jeu_create"), data)

    assert response.status_code == 302

    game_count = JeuDePlateau.objects.filter(
        name=data["name"], createur=data["createur"]
    ).count()
    assert game_count == 1


@pytest.mark.django_db
def test_book_update_get(client, staff_user):
    client.login(username="staff_user", password="password123")
    book = Book.objects.create(name="Test Book")

    response = client.get(reverse("book_update", args=[book.id]))

    assert response.status_code == 200
    assert "Test Book" in response.content.decode()


@pytest.mark.django_db
def test_book_update_post(client, staff_user):
    client.login(username="staff_user", password="password123")
    book = Book.objects.create(name="Test Book", auteur="Test Author")

    updated_data = {"name":"Updated Book","auteur": "Updated Author"}

    response = client.post(reverse("book_update", args=[book.id]), updated_data)

    assert response.status_code == 302

    updated_book = Book.objects.get(id=book.id)
    assert updated_book.auteur == "Updated Author"


@pytest.mark.django_db
def test_dvd_update_get(client, staff_user):
    client.login(username="staff_user", password="password123")
    dvd = Dvd.objects.create(name="Test Dvd")

    response = client.get(reverse("dvd_update", args=[dvd.id]))

    assert response.status_code == 200
    assert "Test Dvd" in response.content.decode()


@pytest.mark.django_db
def test_dvd_update_post(client, staff_user):
    client.login(username="staff_user", password="password123")
    dvd = Dvd.objects.create(name="Test dvd")

    updated_data = {"name": "Updated Dvd", "realisateur":"Updated Director"}

    response = client.post(reverse("dvd_update", args=[dvd.id]), updated_data)

    assert response.status_code == 302

    updated_dvd = Dvd.objects.get(id=dvd.id)
    assert updated_dvd.name == "Updated Dvd"


@pytest.mark.django_db
def test_cd_update_get(client, staff_user):
    client.login(username="staff_user", password="password123")
    cd = Cd.objects.create(name="Test Cd")

    response = client.get(reverse("cd_update", args=[cd.id]))

    assert response.status_code == 200
    assert "Test Cd" in response.content.decode()


@pytest.mark.django_db
def test_cd_update_post(client, staff_user):
    client.login(username="staff_user", password="password123")
    cd = Cd.objects.create(name="Test Cd")

    updated_data = {"name": "Updated Cd", "artiste": "Updated Artist"}

    response = client.post(reverse("cd_update", args=[cd.id]), updated_data)

    assert response.status_code == 302

    updated_cd = Cd.objects.get(id=cd.id)
    assert updated_cd.name == "Updated Cd"


@pytest.mark.django_db
def test_jeu_update_get(client, staff_user):
    client.login(username="staff_user", password="password123")
    game = JeuDePlateau.objects.create(name="Test Game")

    response = client.get(reverse("jeu_update", args=[game.id]))

    assert response.status_code == 200
    assert "Test Game" in response.content.decode()


@pytest.mark.django_db
def test_game_update_post(client, staff_user):
    client.login(username="staff_user", password="password123")
    game = JeuDePlateau.objects.create(name="Test game")

    updated_data = {"name": "Updated game", "createur": "Updated Creator"}

    response = client.post(reverse("jeu_update", args=[game.id]), updated_data)

    assert response.status_code == 302

    updated_game = JeuDePlateau.objects.get(id=game.id)
    assert updated_game.name == "Updated game"


@pytest.mark.django_db
def test_media_delete(client, staff_user):
    client.login(username="staff_user", password="password123")
    book = Book.objects.create(name="Test book")

    url = reverse("media_delete", args=[book.id])

    response = client.post(url)

    assert response.status_code == 302
    assert Media.objects.filter(id=book.id).exists() == False


@pytest.mark.django_db
def test_jeu_delete(client, staff_user):
    client.login(username="staff_user", password="password123")
    game = JeuDePlateau.objects.create(name="Test game")

    url = reverse("jeu_delete", args=[game.id])

    response = client.post(url)

    assert response.status_code == 302
    assert JeuDePlateau.objects.filter(id=game.id).exists() == False


@pytest.mark.django_db
def test_user_create(client, staff_user):
    client.login(username="staff_user", password="password123")
    data = {
        "username": "John",
        "first_name": "John",
        "last_name": "Doe",
        "password": "password",
    }

    response = client.post(reverse("user_create"), data)

    assert response.status_code == 302

    user_count = User.objects.filter(
        username=data["username"], first_name=data["first_name"], last_name=data["last_name"]
    ).count()
    assert user_count == 1


@pytest.mark.django_db
def test_user_update_get(client, staff_user):
    client.login(username="staff_user", password="password123")
    user = User.objects.create(username="Test Name")

    response = client.get(reverse("user_update", args=[user.id]))

    assert response.status_code == 200
    assert "Test Name" in response.content.decode()


@pytest.mark.django_db
def test_user_delete(client, staff_user):
    client.login(username="staff_user", password="password123")
    user = User.objects.create(username="Test Name")

    url = reverse("user_delete", args=[user.id])

    response = client.post(url)

    assert response.status_code == 302
    assert User.objects.filter(id=user.id).exists() == False