from django.db import models


class Menu(models.Model):
    """
    菜单表
    """
    # title 需要创建唯一索引, 不允许重复
    title = models.CharField(verbose_name='菜单标题', max_length=32, unique=True)
    icon = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)
    name = models.CharField(verbose_name="权限别名,用于页面按钮控制", max_length=32, null=True, blank=True)

    pid = models.ForeignKey(verbose_name="父权限归属", to="Permission", null=True, blank=True, on_delete=models.CASCADE)
    # 关联菜单表: 一对多 -----
    menu = models.ForeignKey(verbose_name='所属菜单', to='Menu', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色
    """
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)
    roles = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)

    def __str__(self):
        return self.name
