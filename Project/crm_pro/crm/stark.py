from stark.service.stark import StarkConfig, site, Option, display_chioces
from crm.models import Department, UserInfo, Course, School, ClassList, Customer
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import HttpResponse, reverse, redirect, render
from django import forms


# 部门管理
class DepartConfig(StarkConfig):

    list_display = ["id", "title", StarkConfig.display_edit, StarkConfig.display_del]


site.register(Department, DepartConfig)


# 用户管理
class UserInfoConfig(StarkConfig):

    # 显示choices 已被公共 闭包 display_chioces代替

    # def display_gender(self, row=None, header=False):
    #
    #     if header:
    #         return "性别"
    #
    #     return row.get_gender_display()

    """定制详情页面"""
    # 1.显示详细页面
    def display_detail(self, row=None, header=False):
        if header:
            return "姓名"
        url = reverse("stark:crm_userinfo_detail", kwargs={"pk": row.pk})

        return mark_safe("<a href='{}'>{}</a>".format(url, row.tname))

    # 2.定制详细页面的url
    def extra_url(self):
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        urlpatterns = [
            url(r'^(?P<pk>\d+)/detail/', self.wrapper(self.detail_view), name='%s_%s_detail' % info),
        ]
        return urlpatterns

    # 3.定制详细页面视图
    def detail_view(self, request, pk):

        obj = self.model_class.objects.filter(pk=pk).first()

        return HttpResponse("{}的详细页面".format(obj.name))

    # 配置list页面显示表格内容
    list_display = ["id", display_detail, "phone", display_chioces("gender", "性别"), "depart", StarkConfig.display_edit_del]

    # 添加搜索功能, 外键字段需要使用双下划线来获取
    search_list = ["tname", "depart__title"]


site.register(UserInfo, UserInfoConfig)


# 课程管理
class CourseConfig(StarkConfig):
    list_display = ["id", "name", StarkConfig.display_edit, StarkConfig.display_del]


site.register(Course, CourseConfig)


# 校区管理
class SchoolConfig(StarkConfig):
    list_display = ["id", "title", StarkConfig.display_edit, StarkConfig.display_del]


site.register(School, SchoolConfig)


# 班级管理
class ClassListConfig(StarkConfig):

    # 定制表格班级标题: 如  Python全栈-12期
    def display_title(self, row=None, header=False):
        if header:
            return "班级"

        return "{}-{}期".format(row.course.name, row.semester)

    # 定制表格输出时间字段格式化
    def display_str(self, row=None, header=False):
        if header:
            return "开班日期"

        return row.start_date.strftime("%Y-%m-%d")

    list_display = ["id", display_title, "school", display_str, StarkConfig.display_edit, StarkConfig.display_del]

    # 定制组合搜索
    list_filter = [                        # 组合搜索按钮文字显示         #  组合搜索按钮点击 提交 id:course=2&school=2
        Option("school", is_choice=False, text_func=lambda x: x.title, value_func=lambda x:x.pk, is_multi=False),
        Option("course", is_choice=False, text_func=lambda x: x.name, value_func=lambda x:x.pk, is_multi=False),
    ]


site.register(ClassList, ClassListConfig)


# 客户管理
class CustomerConfig(StarkConfig):
    # 表格显示字段
    list_display = [
        "name",
        display_chioces("gender", "性别"),
        "qq",
        display_chioces("status", "状态"),
        display_chioces("source", "来源"),
        StarkConfig.display_edit,
        StarkConfig.display_del,
    ]

    # 显示排序
    order_by = ["-id"]

    # 模糊搜索
    search_list = ["name", "qq"]

    # 组合搜索
    list_filter = [
        Option("status", is_choice=True, text_func=lambda x: x[1]),
        Option("gender", is_choice=True, text_func=lambda x: x[1]),
        Option("education", is_choice=True, text_func=lambda x: x[1]),
        Option("source", is_choice=True, text_func=lambda x: x[1]),
    ]


# 客户管理- 公有用户管理
class PubModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('consultant',)  # 排除字段, 使得表单上不显示


class PubCustomerConfig(StarkConfig):
    # 表格显示字段
    list_display = [
        "name",
        display_chioces("gender", "性别"),
        "qq",
        display_chioces("status", "状态"),
        display_chioces("source", "来源"),
        StarkConfig.display_edit
    ]

    # 显示排序
    order_by = ["-id"]

    # 模糊搜索
    search_list = ["name", "qq"]

    # 组合搜索
    list_filter = [
        Option("status", is_choice=True, text_func=lambda x: x[1]),
        Option("gender", is_choice=True, text_func=lambda x: x[1]),
        Option("education", is_choice=True, text_func=lambda x: x[1]),
    ]

    # 模型表单
    model_form_class = PubModelForm

    # 获取查询集, 提前筛选, 公有客户筛选
    def get_queryset(self):

        return self.model_class.objects.filter(consultant__isnull=True)


# 客户管理 - 私有用户管理
class PriModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('consultant',)


class PriCustomerConfig(StarkConfig):
    # 表格显示字段
    list_display = [
        "name",
        display_chioces("gender", "性别"),
        "qq",
        display_chioces("status", "状态"),
        display_chioces("source", "来源"),
        StarkConfig.display_edit
    ]

    # 显示排序
    order_by = ["-id"]

    # 模糊搜索
    search_list = ["name", "qq"]

    # 组合搜索
    list_filter = [
        Option("status", is_choice=True, text_func=lambda x: x[1]),
        Option("gender", is_choice=True, text_func=lambda x: x[1]),
        Option("education", is_choice=True, text_func=lambda x: x[1]),
    ]

    # 表单模型
    model_form_class = PriModelForm

    # 获取查询集, 提前筛选, 私有客户筛选
    def get_queryset(self):
        # 私有客户由 登录账号 来进行筛选
        current_id = 3

        return self.model_class.objects.filter(consultant_id=current_id)

    # 添加私有客户, 不需要填写consultant, 默认添加登录账户的id
    def save_form(self, form, modify=False):
        current_id = 3  # 需要从session中获取登录信息
        # form.instance.consultant_id = current_id
        form.instance.consultant = UserInfo.objects.filter(id=current_id).first()
        form.save()


site.register(Customer, CustomerConfig)
site.register(Customer, PubCustomerConfig, "pub")
site.register(Customer, PriCustomerConfig, "pri")
