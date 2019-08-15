from django.db import models
from app01.models import Role

# Create your models here


class User(models.Model):
    level_choices = (
        (1, "高级"),
        (2, "中级"),
        (3, "低级")
    )

    name = models.CharField(max_length=32, verbose_name="用户名", unique=True)
    telephone = models.CharField(max_length=11, verbose_name="移动电话", blank=True, null=True)
    area = models.CharField(max_length=32, verbose_name="地址", blank=True, null=True)
    level = models.IntegerField(verbose_name="等级", choices=level_choices, default=2)
    depart = models.ForeignKey(to="Depart", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):

        return self.name

class Depart(models.Model):

    name = models.CharField(max_length=32, verbose_name="部门", unique=True)

    tel = models.CharField(max_length=32, verbose_name="部门电话", unique=True)

    def __str__(self):

        return self.name