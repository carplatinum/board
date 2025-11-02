import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
def test_ads_list():
    client = APIClient()
    url = reverse("ads:ads-list")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_ads_create_requires_auth():
    client = APIClient()
    url = reverse("ads:ads-list")
    data = {
        "title": "Simple Ad",
        "description": "Simple description",
        "price": "10.00",
    }
    # Без авторизации POST должен быть запрещён
    response = client.post(url, data, format="json")
    assert response.status_code in (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN)
