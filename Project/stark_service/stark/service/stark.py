"""三.
     怎么样生成应用的url?

     需要使用単例模式, 来生成一个实例对象来管理应用模型获取urls;

     需要面向对象编程 多态 来针对不同的应用实现不同的urls功能

"""
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, reverse, redirect
from types import FunctionType
from django.utils.safestring import mark_safe
from django import forms
from django.db.models import Q, ForeignKey
from utils.pagination import Pagination
from .combsearce import CombSearch


class StarkConfig:
    """模型类的默认url生成配置"""
    order_by_list = []  # 通过继承类覆盖该字段可以自定以排序 order_by_list = ["-id]
    list_display = []  # 通过继承类覆盖该字段可以自定以 显示字段
    search_list = ["id", "name", "area"]
    search_field = []
    def __init__(self, model_class, site):
        self.model_class = model_class
        self.site = site

    @property
    def urls(self):
        return self.get_urls()

    def get_urls(self):
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        # 这里的url定位到视图
        urlpatterns = [
            url(r'^list/$', self.changlist_view, name="%s_%s_changelist" % info),
            url(r'^add/$', self.add_view, name='%s_%s_add' % info),
            url(r'^(?P<pk>\d+)/change/$', self.change_view, name='%s_%s_change' % info),
            url(r'^(?P<pk>\d+)/del/$', self.delete_view, name='%s_%s_del' % info),
        ]

        # 上述为固定url地址, 那如果想扩展其他url地址呢?
        # 通过设计继承自StarkConfig类,并重写extra_url()方法来定义
        extra = self.extra_url()

        if extra:
            # extra为可迭代对象
            urlpatterns.extend(extra)

        return urlpatterns

    def extra_url(self):
        """
            预留函数, 可用于扩展url地址

            urlpatterns = [
            url(r'^list/$', self.changlist_view, name="%s_%s_changelist" % info),
            url(r'^add/$', self.add_view, name='%s_%s_add' % info),
            ]

            自定义类继承, 重写该方法, 并返回上述例子urlpatterns以及, 提供对应视图, 即可自动生成路由
        :return:
        """
        return False

    def get_list_display(self):
        """
            预留的钩子函数, 可以进行显示字段的控制

            同样是继承类进行重写即可使用
        :return:
        """
        return self.list_display

    def get_search_list(self):
        val = []
        if self.search_list:
            val.extend(self.search_list)

        return val

    """定制相关功能按键"""
    def get_display_url(self, row=None):
        """
            获取反向解析所需要的  namespace & 组织别名的数据
        :param row:
        :return:
        """
        namespace = self.site.namespace
        app_label = self.model_class._meta.app_label
        model_name = self.model_class._meta.model_name

        return namespace, app_label, model_name

    def display_checkbox(self, row=None, header=None):
        """
            3.自定义表格第一列 checkbox
            问题: 如果每一个子类都需要这个定制呢? 可以将该功能放到StarkConfig下
        :param row:
        :param header:
        :return:
        """
        if header:

            return "选择"
        return mark_safe('<input type="checkbox" name="pk" value=%s >' % row.pk)

    def display_edit(self, row=None, header=None):
        """
            4. 自定义表格 编辑 功能

            url生成  技术点: 反向生成url
        :param row:
        :param header:
        :return:
        """
        if header:

            return "编辑"

        reverse_name = self.get_display_url(row)
        name = '{}:{}_{}_change'.format(*reverse_name)

        edit_url = reverse(name, kwargs={"pk": row.pk})
        tmp =mark_safe('<a href="{}"><i class="fa fa-edit" aria-hidden="true"></i></a>'.format(edit_url))

        return tmp

    def display_del(self, row=None, header=None):
        """
            4. 自定义表格 编辑 功能

            url生成  技术点: 反向生成url
        :param row:
        :param header:
        :return:
        """
        if header:

            return "编辑"

        reverse_name = self.get_display_url(row)
        name = '{}:{}_{}_del'.format(*reverse_name)
        del_url = reverse(name, kwargs={"pk": row.pk})
        tmp =mark_safe('<a href="{}"><i class="fa fa-trash-o" aria-hidden="true"></i></a>'.format(del_url))

        return tmp

    def display_edit_del(self, row=None, header=None):
        """
            4. 自定义表格 编辑 功能

            url生成  技术点: 反向生成url
        :param row:
        :param header:
        :return:
        """
        if header:

            return "编辑"

        reverse_name = self.get_display_url(row)

        name_del = '{}:{}_{}_del'.format(*reverse_name)
        name_change = '{}:{}_{}_change'.format(*reverse_name)
        del_url = reverse(name_del, kwargs={"pk": row.pk})
        edit_url = reverse(name_change, kwargs={"pk": row.pk})
        tmp =mark_safe('<a href="{}"><i class="fa fa-edit" aria-hidden="true"></i></a> '
                       '<a href="{}"><i class="fa fa-trash-o" aria-hidden="true"></i></a>'.format(edit_url, del_url))

        return tmp

    def display_add_btn(self):
        """
            列表页的添加按钮
        :param need:
        :return:
        """
        namespace_app_model = self.get_display_url()

        add_url = "{}:{}_{}_add".format(*namespace_app_model)

        return mark_safe('<a href="{}" class="btn btn-success">添加</a>'.format(reverse(add_url)))

    def multi_delete(self, request):
        """
            批量删除
        :param request:
        :return:
        """
        pk_list = request.POST.getlist('pk')
        self.model_class.objects.filter(pk__in=pk_list).delete()
        return HttpResponse('删除成功')

    multi_delete.text = "批量删除"

    def multi_init_data(self):

        pass

    multi_init_data.text = "批量初始化"

    multi_action = [multi_delete, multi_init_data]  # 批量操作相关行为,通过自定义相关行为的 方法添加即可

    def display_multi_action(self):
        """
            获取批量行为操作
        :return:
        """
        return self.multi_action

    def search_box(self, request):
        search_list = self.get_search_list()
        q_val = request.GET.get("q", "")  # 获取搜索条件, 默认为空
        # 根据条件进行搜索, 需要使用Q对象
        q_obj = Q()
        # 怎么样带上条件进行返回
        q_obj.connector = "OR"
        if q_val:

            for field in search_list:
                q_obj.children.append(('%s__contains' % field, q_val))

            return search_list, q_val, q_obj

        return search_list, q_val, q_obj

    """定义url相关视图"""
    def get_model_form_class(self):
        """
            自定义配置表单模型
        :return:
        """
        class ModelFormClass(forms.ModelForm):
            class Meta:
                model = self.model_class
                fields = "__all__"

        return ModelFormClass

    def get_row_data(self, queryset, list_display):
        """
            技术点: 生成器

            为了节约从数据库获取数据(大量数据)的内存占用, 当需要使用数据时, 再生成; 使用后被作为垃圾回收;
        :return:
        """
        for item in queryset:
            row = []
            if list_display:
                for name_function in list_display:
                    if isinstance(name_function, FunctionType):
                        val = name_function(self, row=item)
                    else:
                        # 技术点: 反射; 通过字符串获取对象的属性
                        val = getattr(item, name_function)
                    row.append(val)
            else:
                row.append(item)

            yield row

    def changlist_view(self, request):

        # post请求, 批量操作处理
        if request.method == "POST":
            action = request.POST.get("action")

            if action not in [i.__name__ for i in self.display_multi_action()]:

                return HttpResponse("非法请求")
            print(action)
            getattr(self, action)(request)

        # 获取数据库中所有数据,排序
        queryset = self.model_class.objects.all().order_by(*self.order_by_list)

        # 搜索框的实现
        search_list, q, con = self.search_box(request)

        # 组合搜索功能实现
        #
        cs = CombSearch(self.search_field, request, self.model_class)
        combpage = cs.get_search_page()
        combcondition = cs.get_filter_condition()


        # 分页展示
        # 1.获取总数
        total_data = self.model_class.objects.filter(con).count()
        # 2.从request对象获取请求相关信息
        query_params = request.GET.copy()
        # 3.设置查询参数可更改
        query_params._mutable = True

        page = Pagination(request.GET.get("page"), total_data, request.path_info, query_params, per_page=5)

        # 表格显示数集
        queryset = self.model_class.objects.filter(con).filter(**combcondition).order_by(*self.order_by_list).distinct()[page.start:page.end]
        # 显示字段的获取
        list_display = self.get_list_display()
        heard_list = []

        # 为了使用可自定义的显示字段,默认的list_display为[]
        if list_display:
            for name_function in list_display:
                if isinstance(name_function, FunctionType):
                    verbose_name = name_function(self, header=True)
                else:
                    # _meta.get_field()方法,通过传入字段名获取字段对象
                    verbose_name = self.model_class._meta.get_field(name_function).verbose_name
                heard_list.append(verbose_name)
        else:
            # 默认是已模型类名作为表格显示字段title, model类中需要__str__方法.
            heard_list.append(self.model_class._meta.model_name)

        # 组织流向templates的数据
        data_list = self.get_row_data(queryset, list_display)

        # 动态生成的添加按钮
        add_btn = self.display_add_btn()

        # 动态生成批量操作
        multi_act = self.display_multi_action()
        multi_act = [{"name": item.__name__, "text": item.text} for item in multi_act]

        return render(request, "stark/changelist.html", {"data_list": data_list,
                                                         "title_list": heard_list,
                                                         "add_btn": add_btn,
                                                         "multi_act": multi_act,
                                                         "search_list": search_list,
                                                         "q": q,
                                                         "page": page,
                                                         "comb_list": combpage})

    def add_view(self, request):
        """
            添加按钮视图
        :param request:
        :return:
        """
        ModelFormClass = self.get_model_form_class()

        if request.method == "GET":

            modelform = ModelFormClass()

            return render(request, "stark/change.html", {"form": modelform})

        modelform = ModelFormClass(request.POST)

        if modelform.is_valid():

            modelform.save()

            return redirect(reverse("{}:{}_{}_changelist".format(*self.get_display_url())))

        return render(request, "stark/change.html", {"form": modelform})

    def change_view(self, request, pk):

        obj = self.model_class.objects.filter(pk=pk).first()
        if not obj:

            return HttpResponse("数据不存在")

        ModelFormClass = self.get_model_form_class()
        if request.method == "GET":
            modelform = ModelFormClass(instance=obj)

            return render(request, "stark/change.html", {"form": modelform})

        modelform = ModelFormClass(request.POST, instance=obj)

        if modelform.is_valid():
            modelform.save()

            return redirect(reverse("{}:{}_{}_changelist".format(*self.get_display_url())))

        return render(request, "stark/change.html", {"form": modelform})

    def delete_view(self, request, pk):
        obj = self.model_class.objects.filter(pk=pk).first()

        if not obj:

            return HttpResponse("数据不存在")

        obj.delete()

        return redirect(reverse("{}:{}_{}_changelist".format(*self.get_display_url())))


class AdminSite:
    """
        注册应用, 来获取应用的url
    """
    def __init__(self):

        self._registry = {}
        self.app_name = 'stark'
        self.namespace = 'stark'

    def registry(self, model_class, stark_config=None):
        """
            注册模型类
        :param model_class: 模型类
        :param stark_config: 模型类相应的配置,None表示按默认配置类生成url
        :return:
        self._registry结构:
        {
            models.UserInfo: StarkConfig(models.UserInfo), # 封装：model_class=UserInfo，site=site对象
            models.Role: RoleConfig(models.Role)           # 封装：model_class=Role，site=site对象
        }
        """
        if not stark_config:
            stark_config = StarkConfig

        self._registry[model_class] = stark_config(model_class, self)

    @property  # 实现方法类似于属性调用 对象.urls 来获取方法的返回值
    def urls(self):

        return self.get_urls(), self.app_name, self.namespace

    def get_urls(self):
        urlpatterns = []

        for k, v in self._registry.items():
            app_label = k._meta.app_label  # 通过模型类获取所在应用名
            model_name = k._meta.model_name  # 获取模型类对应表名
            # 这里类似于在路由分发, 生成url地址的前缀部分,例子: user/role/ 用户的角色表
            urlpatterns.append(
                url(
                    (r'^%s/%s/') % (app_label, model_name),
                    (v.urls, None, None),
                )
            )

        return urlpatterns


site = AdminSite()

