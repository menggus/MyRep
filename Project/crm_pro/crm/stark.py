from stark.service.stark import StarkConfig, site, Option, display_chioces
from crm.models import Department, UserInfo, Course, School, ClassList, Customer, ConsultRecord, Student, StudyRecord, CourseRecord
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import HttpResponse, reverse, redirect, render
from django import forms
from django.conf import settings
from django.db import transaction


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
    # 跟进记录显示
    def display_consultrecord(self, row=None, header=False):
        if header:
            return "跟进记录"
        url = reverse("stark:crm_consultrecord_list")

        return mark_safe('<a href="{}?cid={}">跟进记录</a>'.format(url, row.pk))

    # 表格显示字段
    list_display = [
        "name",
        display_chioces("gender", "性别"),
        "qq",
        display_chioces("status", "状态"),
        display_chioces("source", "来源"),
        display_consultrecord,
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
    # 跟进记录显示
    def display_consultrecord(self, row=None, header=False):
        if header:
            return "跟进记录"
        url = reverse("stark:crm_consultrecord_pub_list")

        return mark_safe('<a href="{}?cid={}">跟进记录</a>'.format(url, row.pk))

    # 表格显示字段
    list_display = [
        StarkConfig.display_checkbox,
        "name",
        display_chioces("gender", "性别"),
        "qq",
        display_chioces("status", "状态"),
        display_consultrecord,
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

    # 批量添加公户到私户
    def multi_add(self, request):
        pk_list = request.POST.getlist('pk')
        current_id = 4

        # 最大私有客户数判断
        private_customer_count = self.model_class.objects.filter(consultant_id=current_id, status=2).count()
        if len(pk_list) + private_customer_count > settings.MAX_PRIVATE_CUSTOMER:
            return HttpResponse("您的私有客户超出最大值, 此次申请失败")

        # 数据库操作-事务
        flage = False
        with transaction.atomic():
            # 没有被分配顾问的客户 和 申请客户数是否一致的判断
            objs_queryset = self.model_class.objects.filter(pk__in=pk_list, consultant__isnull=True)
            if len(pk_list) == len(objs_queryset):
                objs_queryset.update(consultant_id=current_id)
                flage = True
        if not flage:
            return HttpResponse("申请客户中存在已被申请的客户, 请刷新重试....")

    multi_add.text = "批量申请"

    action_list = [multi_add]


# 客户管理 - 私有用户管理
class PriModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('consultant',)


class PriCustomerConfig(StarkConfig):
    # 跟进记录显示
    def display_consultrecord(self, row=None, header=False):
        if header:
            return "跟进记录"
        url = reverse("stark:crm_consultrecord_pri_list")

        return mark_safe('<a href="{}?cid={}">跟进记录</a>'.format(url, row.pk))

    # 表格显示字段
    list_display = [
        StarkConfig.display_checkbox,
        "name",
        display_chioces("gender", "性别"),
        "qq",
        display_chioces("status", "状态"),
        display_consultrecord,
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
        current_id = 4

        return self.model_class.objects.filter(consultant_id=current_id)

    # 添加私有客户, 不需要填写consultant, 默认添加登录账户的id
    def save_form(self, form, modify=False):
        current_id = 4  # 需要从session中获取登录信息
        # form.instance.consultant_id = current_id
        if not modify:
            form.instance.consultant = UserInfo.objects.filter(id=current_id).first()
        form.save()

    # 批量移除私户到公户, 设置consultant_id=None即可变为公有
    def multi_remove(self, request):
        pk_list = request.POST.getlist('pk')
        current_id = 4
        queryset = self.model_class.objects.filter(pk__in=pk_list, status=2, consultant_id=current_id)
        if len(pk_list) == len(queryset):
            queryset.update(consultant_id=None)
        else:
            return HttpResponse("不能移除已报名的客户......")

    multi_remove.text = "批量移除"

    action_list = [multi_remove]


site.register(Customer, CustomerConfig)
site.register(Customer, PubCustomerConfig, "pub")
site.register(Customer, PriCustomerConfig, "pri")


# 客户的跟进记录
class ConsultRecordConfig(StarkConfig):

    # 显示字段
    list_display = [
        'customer',
        'consultant',
        'note',
        'date',
    ]

    # 跟进记录页面, 带查询条件
    def get_queryset(self):
        # 无cid: 所有客户跟进记录列表页; 存在cid, 为当前cid的客户跟进记录
        cid = self.request.GET.get("cid")

        if cid:
            return ConsultRecord.objects.filter(customer_id=cid)

        return ConsultRecord.objects


# 公有客户跟进记录
class PubConsultRecordConfig(StarkConfig):

    # 显示字段
    list_display = [
        'customer',
        'consultant',
        'note',
        'date',
    ]

    # 公有客户跟踪记录, 只能查看, 不能添加,修改,删除
    def get_add_btn(self):

        return None

    # 公共客户跟踪记录 查询集为: 所有公户跟踪记录, 带id的公户跟踪记录, 以及公户的跟踪人为None
    def get_queryset(self):
        cid = self.request.GET.get("cid")

        if cid:
            return ConsultRecord.objects.filter(customer_id=cid, customer__consultant=None)

        return ConsultRecord.objects.filter(customer__consultant=None)


# 私有客户跟进记录
class PriConsultRecord(forms.ModelForm):
    class Meta:
        model = ConsultRecord
        exclude = ["customer", "consultant"]


class PriConsultRecordConfig(StarkConfig):
    # 显示字段
    list_display = [
        'customer',
        'consultant',
        'note',
        'date',
        StarkConfig.display_edit_del,
    ]

    # 私有客户跟踪记录的 表单模型类
    model_form_class = PriConsultRecord

    # 跟进记录页面, 带查询条件
    def get_queryset(self):
        # 无cid: 所有客户跟进记录列表页; 存在cid, 为当前cid的客户跟进记录
        cid = self.request.GET.get("cid")
        current_id = 4  # 当前登录用户的id, 需要从session中获取
        if cid:
            # 这里的跟进记录业务逻辑
            # 1.从私人客户页面跳转的 私人跟进记录页面.
            # 跟进记录数据为: 当前跟进人的id(注意: 曾经跟踪过的客户是否需要区分, 这里做了区分)
            return ConsultRecord.objects.filter(customer_id=cid, customer__consultant_id=current_id)

        return ConsultRecord.objects.filter(customer__consultant_id=current_id)

    # 私有客户表单数据保存
    def save_form(self, form, modify=False):
        if not modify:
            # 私有账户添加客户跟踪记录时,由于用户只填写跟踪记录,所以 客户 和 跟踪人 需要默认填写
            params = self.request.GET.get("_filter")
            cid, num = params.split("=", maxsplit=1)
            form.instance.customer = Customer.objects.filter(pk=num).first()
            current_id = 4  # 需要从session中, 获取登录账户id
            form.instance.consultant = UserInfo.objects.filter(pk=current_id).first()
        # 编辑修改, 直接修改跟踪记录即可 客户 和 跟踪人 默认存在值
        form.save()


site.register(ConsultRecord, ConsultRecordConfig)
site.register(ConsultRecord, PubConsultRecordConfig, "pub")
site.register(ConsultRecord, PriConsultRecordConfig, "pri")


# 教学管理

class StudentConfig(StarkConfig):

    def display_classname(self, row=None, header=False):
        if header:
            return "班级"

        classlist = row.class_list.all()

        list_name = ["{}-{}".format(item.course.name, item.semester) for item in classlist]
        return ",   ".join(list_name)

    list_display = ["username", display_classname, StarkConfig.display_edit_del]


site.register(Student, StudentConfig)


# 课程记录
class CourseRecordConfig(StarkConfig):

    def display_courserecord(self, row=None, header=False):
        if header:
            return "上课记录"

        return "{} {}".format(row.class_obj, row.day_num)

    list_display = [StarkConfig.display_checkbox, "class_obj", StarkConfig.display_edit_del]

    def multi_init_courserecord(self, request):

        nid_list = request.POST.getlist("pk")
        # 获取初始化的班级id
        for nid in nid_list:
            course_record_obj = self.model_class.objects.filter(id=nid).first()
            class_id = course_record_obj.class_obj
            # 根据班级查找班级学生,
            stu_objs = Student.objects.filter(class_list=class_id)

            exists = StudyRecord.objects.filter(course_record=course_record_obj).exists()
            if exists:
                continue

            study_record_list = []
            # 为每一个学生初始化一个学习记录
            for stu in stu_objs:
                study_record_list.append(StudyRecord(course_record=course_record_obj, student=stu))

            StudyRecord.objects.bulk_create(study_record_list)

    multi_init_courserecord.text = "批量初始化"

    action_list = [multi_init_courserecord]


site.register(CourseRecord, CourseRecordConfig)