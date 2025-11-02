from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

app_name = "users"  # namespace для приложения

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")  # basename соответствует app_name

urlpatterns = [
    path("", include(router.urls)),
]
