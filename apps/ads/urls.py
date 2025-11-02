from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdViewSet

app_name = "ads"  # namespace для приложения

router = DefaultRouter()
router.register(r"ads", AdViewSet, basename="ads")  # basename соответствует app_name

urlpatterns = [
    path("", include(router.urls)),
]
