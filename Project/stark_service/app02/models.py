from django.db import models
from app01.models import Role

# Create your models here


class User(models.Model):

    name = models.CharField(max_length=32, verbose_name="用户名", unique=True)

    def __str__(self):

        return self.name