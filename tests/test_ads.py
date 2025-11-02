import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.ads.models import Ad
from apps.users.models import User

@pytest.mark.django_db
class TestAdsAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Создаём пользователя-владельца для тестов
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )
        self.client = APIClient()
        # Авторизуем клиента
        self.client.force_authenticate(user=self.user)

    def test_ads_list(self):
        url = reverse("ads-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_ad(self):
        url = reverse("ads-list")
        data = {
            "title": "Test Ad",
            "description": "Test description",
            "price": "99.99",
        }
        response = self.client.post(url, data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        # Проверяем, что объявление создано и владелец совпадает
        ad = Ad.objects.get(title="Test Ad")
        assert ad.owner == self.user
        assert ad.description == "Test description"
        assert str(ad.price) == "99.99"

    def test_update_ad_owner(self):
        # Создаём объявление владельцем
        ad = Ad.objects.create(
            title="Old Title",
            description="Old description",
            price=10.0,
            owner=self.user
        )
        url = reverse("ads-detail", args=[ad.id])
        data = {
            "title": "Updated Title",
            "description": "Updated description",
            "price": "20.00",
        }
        response = self.client.put(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        ad.refresh_from_db()
        assert ad.title == "Updated Title"
        assert ad.price == 20.00

    def test_delete_ad_owner(self):
        ad = Ad.objects.create(
            title="Ad To Delete",
            description="To be deleted",
            price=50.0,
            owner=self.user
        )
        url = reverse("ads-detail", args=[ad.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(Ad.DoesNotExist):
            Ad.objects.get(id=ad.id)

    def test_update_ad_not_owner(self):
        # Создаём другого пользователя и объявление от него
        other_user = User.objects.create_user(
            username="otheruser",
            email="otheruser@example.com",
            password="password123"
        )
        ad = Ad.objects.create(
            title="Other's Ad",
            description="Not owned by testuser",
            price=100,
            owner=other_user
        )
        url = reverse("ads-detail", args=[ad.id])
        data = {"title": "Hacked Title"}
        # Попытка изменения чужого объявления должна быть запрещена
        response = self.client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN
