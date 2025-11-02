import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
def test_users_list_requires_auth():
    client = APIClient()
    url = reverse("users:users-list")
    response = client.get(url)
    # Без авторизации список пользователей недоступен
    assert response.status_code in (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN)
