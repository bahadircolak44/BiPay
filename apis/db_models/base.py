import traceback

from django.db import models
from django.contrib.auth.models import User


class APPModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def get_or_none(cls, **kwargs):
        try:
            cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            return None
        except cls.MultipleObjectsReturned as error:
            print(traceback.format_exc())
            return None

    class Meta:
        abstract = True

