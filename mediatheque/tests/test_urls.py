import pytest

from django.urls import reverse, resolve
from django.test import Client
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from authentication.views import user_login, logout_user
from users.models import User
from media.views import (
    media,
    media_detail,
    jeu_detail,
    book_create,
    dvd_create,
    cd_create,
    jeu_create,
    book_update,
    dvd_update,
    cd_update,
    jeu_update,
    media_delete,
    jeu_delete,
)
from users.views import (users, user_detail, user_create, user_update, user_delete)
from loans.views import (media_loan, loan_impossible, loan_late)

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


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_home_url_staff(client, staff_user):
    client.login(username="staff_user", password="password123")
    response = client.get(reverse("home"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_url_non_staff(client, non_staff_user):
    client.login(username="non_staff_user", password="password123")
    response = client.get(reverse("home"))
    assert response.status_code != 200


@pytest.mark.django_db
def test_url_home_view_non_staff(client, non_staff_user):
    client.login(username="non_staff_user", password="password123")
    response = client.get(reverse("users_home"))
    assert response.status_code == 200


class TestUrlsMedia:

    def setup_method(self, method):
        print('Setup method')

    def teardown_method(self, method):
        print("Teardown method")

    def test_media_url(self):
        path = reverse("media")
        assert resolve(path).func == media

    def test_media_detail_url(self):
        path = reverse("media_detail", args=[1])
        assert resolve(path).func == media_detail

    def test_jeu_detail_url(self):
        path = reverse("jeu_detail", args=[1])
        assert resolve(path).func == jeu_detail

    def test_book_create_url(self):
        path = reverse("book_create")
        assert resolve(path).func == book_create

    def test_cd_create_url(self):
        path = reverse("cd_create")
        assert resolve(path).func == cd_create

    def test_dvd_create_url(self):
        path = reverse("dvd_create")
        assert resolve(path).func == dvd_create

    def test_jeu_create_url(self):
        path = reverse("jeu_create")
        assert resolve(path).func == jeu_create

    def test_book_update_url(self):
        path = reverse("book_update", args=[1])
        assert resolve(path).func == book_update

    def test_dvd_update_url(self):
        path = reverse("dvd_update", args=[1])
        assert resolve(path).func == dvd_update

    def test_cd_update_url(self):
        path = reverse("cd_update", args=[1])
        assert resolve(path).func == cd_update

    def test_jeu_update_url(self):
        path = reverse("jeu_update", args=[1])
        assert resolve(path).func == jeu_update

    def test_media_delete_url(self):
        path = reverse("media_delete", args=[1])
        assert resolve(path).func == media_delete

    def test_jeu_delete_url(self):
        path = reverse("jeu_delete", args=[1])
        assert resolve(path).func == jeu_delete

class TestUrlsUsers:

    def setup_method(self, method):
        print("Setup method")

    def teardown_method(self, method):
        print("Teardown method")

    def test_users_url(self):
        path = reverse("users")
        assert resolve(path).func == users

    def test_user_detail_url(self):
        path = reverse("user_detail", args=[1])
        assert resolve(path).func == user_detail

    def test_user_create_url(self):
        path = reverse("user_create")
        assert resolve(path).func == user_create

    def test_user_update_url(self):
        path = reverse("user_update", args=[1])
        assert resolve(path).func == user_update

    def test_user_delete_url(self):
        path = reverse("user_delete", args=[1])
        assert resolve(path).func == user_delete


class TestUrlsLoans:

    def setup_method(self, method):
        print("Setup method")

    def teardown_method(self, method):
        print("Teardown method")

    def test_media_loan_url(self):
        path = reverse("media_loan", args=[1])
        assert resolve(path).func == media_loan

    def test_loan_impossible_url(self):
        path = reverse("loan_impossible")
        assert resolve(path).func == loan_impossible

    def test_loan_late_url(self):
        path = reverse("loan_late")
        assert resolve(path).func == loan_late


class TestUrlsAuthentication:

    def setup_method(self, method):
        print("Setup method")

    def teardown_method(self, method):
        print("Teardown method")

    @pytest.mark.django_db
    def test_user_login_authenticated(self, client):
        user = User.objects.create_user(username='testuser', password='12345')
        url = reverse('login')
        response = client.post(url, {'username': 'testuser', 'password': '12345'})
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_user_login_invalid(self, client):
        user = User.objects.create_user(username='testuser', password='12345')
        url = reverse('login')
        response = client.post(url, {'username': 'testuser', 'password': 'wrongpassword'})
        assert response.status_code == 200  
        assert b'Identifiants invalides' in response.content  

    @pytest.mark.django_db
    def test_logout_user(self, client):
        url = reverse('logout')
        response = client.get(url)
        assert response.status_code == 302
