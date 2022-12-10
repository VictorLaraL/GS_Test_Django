from rest_framework import response, serializers
from random import randrange
from rest_framework.decorators import action, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from stdnum.mx import rfc, curp
import re
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
            "phone",
            "date",
            "is_admin",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "date": {"read_only": True},             
            "id": {"read_only": True},
        }

    def validate(self, data):
        """
            Validacion de los campos que son necesarios en el sistema.
            Se podria generar un mensaje de acerdo al error si se quiere
            ser mas explicito.
        """
        try:
            rfc.validate(data["rfc"])
        except (rfc.InvalidComponent, rfc.InvalidFormat, rfc.InvalidLength, rfc.InvalidChecksum):
            raise serializers.ValidationError(
                "EL rfc es incorrecto"
                ) 
        try:
            curp.validate(data["curp"])
        except (curp.InvalidComponent, curp.InvalidFormat, curp.InvalidLength, curp.InvalidChecksum):
            raise serializers.ValidationError(
                "EL curp es incorrecto"
                ) 
        
        if re.match(r"\d{5}", str(data["postal_code"])) == None:
            raise serializers.ValidationError(
                "EL codigo postal es incorrecto"
                ) 

        return data


class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermission
        fields = ("id", "user", "permission")