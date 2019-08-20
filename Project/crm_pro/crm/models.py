from django.db import models

# Create your models here.
from rbac.models import UserInfo as RbacUserInfo
from django.db import models


class Department(models.Model):
    """
    部门表
    """
    title = models.CharField(verbose_name='部门名称', max_length=16)

    def __str__(self):
        return self.title


class UserInfo(RbacUserInfo):
    """
    员工表
    """
    name = models.CharField(verbose_name='真实姓名', max_length=16)
    phone = models.CharField(verbose_name='手机号', max_length=32)

    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(verbose_name='性别', choices=gender_choices,default=1)

    depart = models.ForeignKey(verbose_name='部门', to="Department", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    课程表
    如：
        Linux基础
        Linux架构师
        Python自动化
        Python全栈
    """
    name = models.CharField(verbose_name='课程名称', max_length=32)

    def __str__(self):
        return self.name


class School(models.Model):
    """
    校区表
    如：
        北京昌平校区
        上海浦东校区
        深圳南山校区
    """
    title = models.CharField(verbose_name='校区名称', max_length=32)

    def __str__(self):
        return self.title


class ClassList(models.Model):
    """
    班级表
    如：
        Python全栈  面授班  5期  10000  2017-11-11  2018-5-11
    """
    school = models.ForeignKey(verbose_name='校区', to='School', null=True, blank=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(verbose_name='课程名称', to='Course',  null=True, blank=True, on_delete=models.SET_NULL)
    semester = models.IntegerField(verbose_name="班级(期)")  # 11
    price = models.IntegerField(verbose_name="学费")
    start_date = models.DateField(verbose_name="开班日期")
    graduate_date = models.DateField(verbose_name="结业日期", null=True, blank=True)
    # tutor = models.ForeignKey(verbose_name='班主任', to='UserInfo', related_name='classes',limit_choices_to={'depart__title':'教质部'})
    # teachers = models.ManyToManyField(verbose_name='任课老师', to='UserInfo', related_name='teach_classes',limit_choices_to={'depart_id__in':[6,7]})
    memo = models.CharField(verbose_name='说明', max_length=256, blank=True, null=True)

    def __str__(self):
        return "{0}({1}期)".format(self.course.name, self.semester)