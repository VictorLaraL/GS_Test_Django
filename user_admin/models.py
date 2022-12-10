from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.base import Model
from paranoid_model.models import Paranoid
from paranoid_model.manager import ParanoidManager

class UserManager(BaseUserManager, ParanoidManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe proporcionar un email")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        user = self.create_user(email, password, **extra_fields)
        return user

class User(AbstractUser, Paranoid):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, default="")
    username = models.CharField(max_length=150, default="", null=True)
    last_name = models.CharField(max_length=150, default="")
    curp = models.CharField(max_length=50)
    postal_code = models.IntegerField(null=True)
    rfc = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ["name"]

    @property
    def full_name(self):
        full_name = []

        if self.name:
            full_name.append(self.name)

        if self.last_name:
            full_name.append(self.last_name)

        return " ".join(full_name)

class UserPermission(models.Model):
    user = models.ForeignKey("user_admin.User", on_delete=models.CASCADE)
    permission = models.ForeignKey("permission.Permission", on_delete=models.CASCADE)