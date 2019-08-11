from django.db import models

# Create your models here.


class Role(models.Model):

    name = models.CharField(max_length=32, verbose_name="角色名", unique=True)