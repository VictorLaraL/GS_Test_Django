from rest_framework import response, serializers
from random import randrange
from rest_framework.decorators import action, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, UserPermission

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_permissions(self, user):
        """Get and configure data permissions list"""
        list_user_permissions = []
        user_permissions = UserPermission.objects.filter(user=user)

        for user_permission in user_permissions:
            list_user_permissions.append(user_permission.permission.keyword)

        return list_user_permissions

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)
        data["id"] = self.user.id
        data["name"] = self.user.name
        data["last_name"] = self.user.last_name
        data["email"] = self.user.email
        data["is_admin"] = self.user.is_admin
        
        # Add permissions info
        data["permissions"] = self.get_permissions(self.user)

        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", 
            "email",
            "name", 
            "last_name",
            "password",
            "curp",
            "postal_code",
            "rfc",
            "date",
            "is_admin",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "date": {"read_only": True},             
            "id": {"read_only": True},
        }

    def validate(self, attrs):
        data = super().validate(attrs)
        data["curp"] = str(refresh)
        data["postal_code"] = str(refresh.access_token)
        data["rfc"] = self.user.id
        data["phone"] = self.user.last_name
        
        return data
class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermission
        fields = ("id", "user", "permission")