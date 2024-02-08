import pytest

from django.urls import reverse
from django.test import Client
from users.models import User
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_user_infos_view(client):
    client = Client()
    User.objects.create(username="Toto", first_name="Toto", last_name="Toto")
    path = reverse("user_detail", kwargs={"id": 1})
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "user_detail")
