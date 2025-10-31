from rest_framework import serializers
from .models import Ad

class AdSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели объявления.
    """
    owner = serializers.ReadOnlyField(source="owner.email")

    class Meta:
        model = Ad
        fields = ("id", "title", "description", "price", "owner", "created_at")
        read_only_fields = ("id", "owner", "created_at")
