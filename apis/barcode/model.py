from django.contrib.auth.models import User
from django.db import models

from apis.db_models.base import APPModel


class Barcode(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    barcode_number = models.CharField(null=False, unique=True, max_length=8)

    class Meta:
        db_table = "barcode"
