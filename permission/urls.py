from django.urls import path, include
from .views import PermissionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'permission', PermissionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
