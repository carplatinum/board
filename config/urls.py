from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    # JWT токены
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Подключение приложений с namespace
    path("api/ads/", include(("apps.ads.urls", "ads"), namespace="ads")),
    path("api/users/", include(("apps.users.urls", "users"), namespace="users")),
]
