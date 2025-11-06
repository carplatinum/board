import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.users.models import User


@pytest.mark.django_db
class TestUsersAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Создает тестового пользователя и аутентифицирует API-клиент.
        """
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_users_list(self):
        """
        Проверяет получение списка всех пользователей.
        """
        url = reverse("users:users-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, list) or "results" in response.data

    def test_create_user(self):
        """
        Проверяет создание нового пользователя.
        """
        url = reverse("users:users-list")
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newstrongpassword"
        }
        response = self.client.post(url, data, format="json")
        assert response.status_code in [status.HTTP_201_CREATED, status.HTTP_403_FORBIDDEN]

    def test_get_user_detail(self):
        """
        Проверяет получение данных конкретного пользователя по ID.
        """
        url = reverse("users:users-detail", args=[self.user.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == self.user.email

    def test_update_user(self):
        """
        Проверяет частичное обновление данных пользователя.
        """
        url = reverse("users:users-detail", args=[self.user.id])
        data = {
            "username": "updatedusername"
        }
        response = self.client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        self.user.refresh_from_db()
        assert self.user.username == "updatedusername"

    def test_delete_user(self):
        """
        Проверяет удаление пользователя или корректную обработку отказа.
        """
        url = reverse("users:users-detail", args=[self.user.id])
        response = self.client.delete(url)
        assert response.status_code in [status.HTTP_204_NO_CONTENT, status.HTTP_403_FORBIDDEN]
        if response.status_code == status.HTTP_204_NO_CONTENT:
            from django.core.exceptions import ObjectDoesNotExist
            with pytest.raises(ObjectDoesNotExist):
                User.objects.get(id=self.user.id)
