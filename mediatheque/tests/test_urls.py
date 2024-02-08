import pytest

from django.urls import reverse, resolve
from users.models import User


@pytest.mark.django_db
def test_user_add_url():
    User.objects.create(
        username="JohnDoe", first_name="John", last_name="Doe", password="password"
    )
    path = reverse("user_detail", kwargs={"id": 1})
    assert path == "/user/users/1/"
    assert resolve(path).view_name == "user_detail"
