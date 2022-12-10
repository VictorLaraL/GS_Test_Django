from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Permission
from .serializers import PermissionSerializer

class PermissionViewSet(viewsets.ModelViewSet):

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['keyword']
    