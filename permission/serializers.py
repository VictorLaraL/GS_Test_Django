from .models import Permission
from rest_framework import response, serializers

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("id", "keyword", "description")