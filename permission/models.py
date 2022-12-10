from django.db import models

class Permission(models.Model):
    keyword = models.CharField(max_length=250, unique=True)
    description = models.TextField(null=True, blank=True)