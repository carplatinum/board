from django.contrib import admin
from .models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
    Админка для модели объявления.
    """
    list_display = ("title", "price", "owner", "created_at")
    list_filter = ("created_at",)
    search_fields = ("title", "description")
