from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import User, UserPermission
from .serializers import UserSerializer, UserPermissionSerializer, UserTokenObtainPairSerializer


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', "email"]

class UserPermissionViewSet(viewsets.ModelViewSet):
    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user__name', "user__email", "permission__keyword"]