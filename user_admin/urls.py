from django.urls import path, include
from .views import UserViewSet, UserPermissionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'userpermission', UserPermissionViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
