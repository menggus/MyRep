## CRUD组件

参考: Django admin;
思考: Django admin 是怎样自动生成增删改查的?

### 知识点一:  autodiscover_modules()
- 自动发现模型方法
- 类似于Django启动会自动去查找admin.py文件,同样是为了找到哪些APP为模型配置了admin的操作
- 查找每一个app下的admin.py文件,同样是使用autodiscover_modules()方法
- CRUD组件, 同样是为了查找stark.py来查找模型配置文件
```python
from django.apps import AppConfig


class StarkConfig(AppConfig):
    name = 'stark'

    def ready(self):
        from django.utils.module_loading import autodiscover_modules
        # 当程序启动时，去每个app目录下找stark.py并加载。
        autodiscover_modules('stark')
```

### 知识点二: 路由分发stark.site.urls
- 项目主url中的路由分发参数 为一个 "元组", 我们同样可以传入一个元组, 同样来实现路由分发
- 元组:  (urls,  app_name, namespace )
```python
urlpatterns = [
    url('admin/', admin.site.urls),
    url('stark/', site.urls),  # 这个就是stark.py中的site, 下面会介绍, site.urls也是一个元组,与admin.site.urls数据结构一样.
    url('rbac/', include(("rbac.urls", 'rbac'), namespace='rbac')),  # django 2.0 需要这么写, 不然会报错
    url('', include(("crm.urls", "crm"), namespace='crm')),
]
```

### 知识点三: 核心AdminSite管理类
- stark组件下的stark.py文件下的类
	- 管理starkcofig, 进行注册登记
	- 获取路由starkconfig中urls, 生产完整的路由地址
		
```python
class AdminSite(object):
    def __init__(self):
        self._registry = []
        self.app_name = 'stark'
        self.namespace = 'stark'

    def register(self, model_class, stark_config=None, pre=None):
        if not stark_config:
            stark_config = StarkConfig  # 默认配置
        # self._registry[model_class] = stark_config(model_class, self)
        # 为了给model配置更多的url, 使得self._registry = []变为列表,存储更多的配置
        self._registry.append(ModelConfigMapping(model_class, stark_config(model_class, self, pre), pre))

    def get_urls(self):

        urlpatterns = []

        for item in self._registry:

            app_label = item.model._meta.app_label
            model_name = item.model._meta.model_name
            # 判断是否有前缀, 根据前缀生产不同的url
            # 这里也做了一次url分发
            if item.pre:
                urlpatterns.append(url(r'^{}/{}/{}/'.format(app_label, model_name, item.pre),
                                       (item.config.urls, None, None)))
            else:
                urlpatterns.append(url(r'^{}/{}/'.format(app_label, model_name,), (item.config.urls, None, None)))
        return urlpatterns

    @property
    def urls(self):

        return self.get_urls(), self.app_name, self.namespace


site = AdminSite()  # 这里是为了在其他app配置stark.py文件中,导入作为单列存在, 同一管理系统的所有配置了的model

```

### 知识点四: StarkConfig默认配置类
- 最终url的生成, 并对应到视图
- 默认的增,删,改,查 视图函数
- 预留功能属性的钩子函数, 比如 默认只有增删改查四种url地址, 如果想增加额外的url, 只需调用extra_url函数中添加新的url即可, extra_url函数会添加到总的urls中.
- 预留配置类属性, 通过配置属性来获取功能
```python
class StarkConfig(object):

    def display_checkbox(self, row=None, header=False):
        if header:
            return "选择"
        return mark_safe("<input type='checkbox' name='pk' value='%s' />" % row.pk)

    def display_edit(self, row=None, header=False):
        if header:
            return "编辑"

        return mark_safe(
            '<a href="%s"><i class="fa fa-edit" aria-hidden="true"></i></a></a>' % self.reverse_edit_url(row))

    def display_del(self, row=None, header=False):
        if header:
            return "删除"

        return mark_safe(
            '<a href="%s"><i class="fa fa-trash-o" aria-hidden="true"></i></a>' % self.reverse_del_url(row))

    def display_edit_del(self, row=None, header=False):
        if header:
            return "操作"
        tpl = """<a href="%s"><i class="fa fa-edit" aria-hidden="true"></i></a></a> |
        <a href="%s"><i class="fa fa-trash-o" aria-hidden="true"></i></a>
        """ % (self.reverse_edit_url(row), self.reverse_del_url(row),)
        return mark_safe(tpl)

    def multi_delete(self, request):
        """
        批量删除的action
        :param request:
        :return:
        """
        pk_list = request.POST.getlist('pk')
        self.model_class.objects.filter(pk__in=pk_list).delete()
        # return HttpResponse('删除成功')

    multi_delete.text = "批量删除"

    order_by = []
    list_display = []
    model_form_class = None
    action_list = []
    search_list = []
    list_filter = []

    def __init__(self, model_class, sites, pre):
        self.model_class = model_class
        self.site = sites
        self.request = None
        self.pre = pre
        self.back_condition_key = "_filter"

    def get_order_by(self):
        return self.order_by

    def get_list_display(self):
        return self.list_display

    def get_add_btn(self):
        return mark_safe('<a href="%s" class="btn btn-success">添加</a>' % self.reverse_add_url())

    def get_model_form_class(self):
        """
            获取ModelForm类
        :return:
        """
        if self.model_form_class:
            return self.model_form_class

        class AddModelForm(forms.ModelForm):
            class Meta:
                model = self.model_class
                fields = "__all__"

        return AddModelForm

    def get_action_list(self):
        val = []
        val.extend(self.action_list)
        return val

    def get_action_dict(self):
        val = {}
        for item in self.action_list:
            val[item.__name__] = item
        return val

    def get_search_list(self):
        val = []
        val.extend(self.search_list)
        return val

    def get_search_condition(self, request):
        search_list = self.get_search_list()  # ['name','tel']
        q = request.GET.get('q', "")  # ‘大’
        con = Q()
        con.connector = "OR"
        if q:
            for field in search_list:
                con.children.append(('%s__contains' % field, q))

        return search_list, q, con

    def get_list_filter(self):
        val = []
        val.extend(self.list_filter)
        return val

    def get_list_filter_condition(self):
        comb_condition = {}
        for option in self.get_list_filter():
            element = self.request.GET.getlist(option.field)
            if element:
                comb_condition['%s__in' % option.field] = element

        return comb_condition

    def get_queryset(self):

        return self.model_class.objects

    def changelist_view(self, request):
        """
        所有URL的查看列表页面
        :param request:
        :return:
        """

        if request.method == 'POST':
            action_name = request.POST.get('action')
            action_dict = self.get_action_dict()
            if action_name not in action_dict:
                return HttpResponse('非法请求')

            response = getattr(self, action_name)(request)
            if response:
                return response

        # ##### 处理搜索 #####
        search_list, q, con = self.get_search_condition(request)

        # ##### 处理分页 #####
        from stark.utils.pagination import Pagination

        total_count = self.model_class.objects.filter(con).count()

        query_params = request.GET.copy()
        query_params._mutable = True
        page = Pagination(request.GET.get('page'), total_count, request.path_info, query_params, per_page=7)


        # 获取组合搜索筛选
        original_queryset = self.get_queryset()
        queryset =original_queryset.filter(con).filter(**self.get_list_filter_condition()).order_by(*self.get_order_by()).distinct()[page.start:page.end]

        cl = ChangeList(self, queryset, q, search_list, page)

        # ######## 组合搜索 #########
        # list_filter = ['name','user']

        context = {
            'cl': cl
        }
        return render(request, 'stark/changelist.html', context)

    def save_form(self, form, modify=False):
        """
            表单提交 数据保存至数据库的钩子函数;
            通过重写, 可重构 form.instance对象(表单数据对象) 的值

        :param form:
        :param modify: add & change 增加和修改; 用于添加时 需要给form.instance对象加入数据, 而修改时, 不需要;
        :return:
        """
        form.save()

    def add_view(self, request):
        """
        所有添加页面，都在此函数处理
        使用ModelForm实现
        :param request:
        :return:
        """
        AddModelForm = self.get_model_form_class()

        if request.method == "GET":
            form = AddModelForm()
            return render(request, 'stark/change.html', {'form': form})

        form = AddModelForm(request.POST)
        if form.is_valid():
            self.save_form(form)
            return redirect(self.reverse_list_url())
        return render(request, 'stark/change.html', {'form': form})

    def change_view(self, request, pk):
        """
        所有编辑页面
        :param request:
        :param pk:
        :return:
        """
        obj = self.model_class.objects.filter(pk=pk).first()
        if not obj:
            return HttpResponse('数据不存在')

        ModelFormClass = self.get_model_form_class()
        if request.method == 'GET':
            form = ModelFormClass(instance=obj)
            return render(request, 'stark/change.html', {'form': form})
        form = ModelFormClass(data=request.POST, instance=obj)
        if form.is_valid():
            self.save_form(form, True)
            return redirect(self.reverse_list_url())
        return render(request, 'stark/change.html', {'form': form})

    def delete_view(self, request, pk):
        """
        所有删除页面
        :param request:
        :param pk:
        :return:
        """
        if request.method == "GET":
            return render(request, 'stark/delete.html', {'cancel_url': self.reverse_list_url()})

        print(self.model_class.objects.filter(pk=pk))

        self.model_class.objects.filter(pk=pk).delete()

        return redirect(self.reverse_list_url())

    def wrapper(self, func):
        @functools.wraps(func)
        def inner(request, *args, **kwargs):
            self.request = request
            return func(request, *args, **kwargs)

        return inner

    # 由 get_reverse_url_name 方法代替
    # def get_list_url_name(self):
    #     app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name
    #     if self.pre:
    #         name = '%s_%s_%s_changelist' % (app_label, model_name, self.pre)
    #     else:
    #         name = '%s_%s_changelist' % (app_label, model_name)
    #     return name
    #
    # def get_add_url_name(self):
    #     app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name
    #     if self.pre:
    #         name = '%s_%s_%s_add' % (app_label, model_name, self.pre)
    #     else:
    #         name = '%s_%s_add' % (app_label, model_name)
    #     return name
    #
    # def get_change_url_name(self):
    #     app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name
    #     if self.pre:
    #         name = '%s_%s_%s_change' % (app_label, model_name, self.pre)
    #     else:
    #         name = '%s_%s_change' % (app_label, model_name)
    #     return name
    #
    # def get_del_url_name(self):
    #     app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name
    #     if self.pre:
    #         name = '%s_%s_%s_del' % (app_label, model_name, self.pre)
    #     else:
    #         name = '%s_%s_del' % (app_label, model_name)
    #     return name  #

    def get_reverse_url_name(self, method):

        app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name
        if self.pre:
            name = '%s_%s_%s_%s' % (app_label, model_name, self.pre, method)
        else:
            name = '%s_%s_%s' % (app_label, model_name, method)
        return name

    def get_urls(self):

        urlpatterns = [
            url(r'^list/$', self.wrapper(self.changelist_view), name=self.get_reverse_url_name("list")),
            url(r'^add/$', self.wrapper(self.add_view), name=self.get_reverse_url_name("add")),
            url(r'^(?P<pk>\d+)/change/', self.wrapper(self.change_view), name=self.get_reverse_url_name("change")),
            url(r'^(?P<pk>\d+)/del/', self.wrapper(self.delete_view), name=self.get_reverse_url_name("del")),
        ]

        extra = self.extra_url()
        if extra:
            urlpatterns.extend(extra)

        return urlpatterns

    @property
    def urls(self):
        return self.get_urls()

    def extra_url(self):
        pass

    def reverse_list_url(self):

        namespace = self.site.namespace
        name = '%s:%s' % (namespace, self.get_reverse_url_name("list"))
        list_url = reverse(name)

        origin_condition = self.request.GET.get(self.back_condition_key)
        if not origin_condition:
            return list_url

        list_url = "%s?%s" % (list_url, origin_condition,)
        return list_url

    def reverse_add_url(self):

        namespace = self.site.namespace
        name = '%s:%s' % (namespace, self.get_reverse_url_name("add"))
        add_url = reverse(name)

        if not self.request.GET:
            return add_url
        param_str = self.request.GET.urlencode()  # q=嘉瑞&page=2
        new_query_dict = QueryDict(mutable=True)
        new_query_dict[self.back_condition_key] = param_str
        add_url = "%s?%s" % (add_url, new_query_dict.urlencode(),)

        return add_url

    def reverse_edit_url(self, row):

        namespace = self.site.namespace
        name = '%s:%s' % (namespace, self.get_reverse_url_name("change"))
        edit_url = reverse(name, kwargs={'pk': row.pk})

        if not self.request.GET:
            return edit_url
        param_str = self.request.GET.urlencode()  # q=嘉瑞&page=2
        new_query_dict = QueryDict(mutable=True)
        new_query_dict[self.back_condition_key] = param_str
        edit_url = "%s?%s" % (edit_url, new_query_dict.urlencode(),)

        return edit_url

    def reverse_del_url(self, row):

        namespace = self.site.namespace
        name = '%s:%s' % (namespace, self.get_reverse_url_name("del"))
        del_url = reverse(name, kwargs={'pk': row.pk})
        # 带上之前url地址的get参数
        if not self.request.GET:
            return del_url

        param_str = self.request.GET.urlencode()
        new_query_dict = QueryDict(mutable=True)
        new_query_dict[self.back_condition_key] = param_str
        del_url = "%s?%s" % (del_url, new_query_dict.urlencode(),)

        return del_url
```
- 反射, yield的使用
```python
from django.template import Library
from types import FunctionType


register = Library()


def header_list(cl):
    """
    表头
    :param cl:
    :return:
    """
    if cl.list_display:
        for name_or_func in cl.list_display:
            if isinstance(name_or_func, FunctionType):
                verbose_name = name_or_func(cl.config, header=True)
            else:
                verbose_name = cl.config.model_class._meta.get_field(name_or_func).verbose_name
            yield verbose_name
    else:
        yield cl.config.model_class._meta.model_name


def body_list(cl):
    """
    表格内容
    :param cl:
    :return:
    """
    for row in cl.queryset:
        row_list = []
        if not cl.list_display:
            row_list.append(row)
            yield row_list
            continue
        for name_or_func in cl.list_display:
            if isinstance(name_or_func, FunctionType):
                val = name_or_func(cl.config, row=row)
            else:
                # 通过反射, 获取row对象中的字段属性
                val = getattr(row, name_or_func)  
            row_list.append(val)
        yield row_list


@register.inclusion_tag('stark/table.html')
def table(cl):

    return {'header_list': header_list(cl), 'body_list': body_list(cl)}
```
- 分页
```python

class Pagination(object):
    def __init__(self, current_page, all_count, base_url, query_params, per_page=10, pager_page_count=11):
        """
        分页初始化
        :param current_page: 当前页码
        :param per_page: 每页显示数据条数
        :param all_count: 数据库中总条数
        :param base_url: 基础URL
        :param query_params: QueryDict对象，内部含所有当前URL的原条件
        :param pager_page_count: 页面上最多显示的页码数量
        """
        self.base_url = base_url
        try:
            self.current_page = int(current_page)
            if self.current_page <= 0:
                raise Exception()
        except Exception as e:
            self.current_page = 1
        self.query_params = query_params
        self.per_page = per_page
        self.all_count = all_count
        self.pager_page_count = pager_page_count
        pager_count, b = divmod(all_count, per_page)
        if b != 0:
            pager_count += 1
        self.pager_count = pager_count

        half_pager_page_count = int(pager_page_count / 2)
        self.half_pager_page_count = half_pager_page_count

    @property
    def start(self):
        """
        数据获取值起始索引
        :return:
        """
        return (self.current_page - 1) * self.per_page

    @property
    def end(self):
        """
        数据获取值结束索引
        :return:
        """
        return self.current_page * self.per_page

    def page_html(self):
        """
        生成HTML页码
        :return:
        """
        # 如果数据总页码pager_count<11 pager_page_count
        if self.pager_count < self.pager_page_count:
            pager_start = 1
            pager_end = self.pager_count
        else:
            # 数据页码已经超过11
            # 判断： 如果当前页 <= 5 half_pager_page_count
            if self.current_page <= self.half_pager_page_count:
                pager_start = 1
                pager_end = self.pager_page_count
            else:
                # 如果： 当前页+5 > 总页码
                if (self.current_page + self.half_pager_page_count) > self.pager_count:
                    pager_end = self.pager_count
                    pager_start = self.pager_count - self.pager_page_count + 1
                else:
                    pager_start = self.current_page - self.half_pager_page_count
                    pager_end = self.current_page + self.half_pager_page_count

        page_list = []

        if self.current_page <= 1:
            prev = '<li><a href="#">上一页</a></li>'
        else:
            self.query_params['page'] = self.current_page - 1
            prev = '<li><a href="%s?%s">上一页</a></li>' % (self.base_url,self.query_params.urlencode())
        page_list.append(prev)
        for i in range(pager_start, pager_end + 1):
            self.query_params['page'] = i
            if self.current_page == i:
                tpl = '<li class="active"><a href="%s?%s">%s</a></li>' % (
                    self.base_url, self.query_params.urlencode(), i,)
            else:
                tpl = '<li><a href="%s?%s">%s</a></li>' % (self.base_url, self.query_params.urlencode(), i,)
            page_list.append(tpl)

        if self.current_page >= self.pager_count:
            nex = '<li><a href="#">下一页</a></li>'
        else:
            self.query_params['page'] = self.current_page + 1
            nex = '<li><a href="%s?%s">下一页</a></li>' % (self.base_url, self.query_params.urlencode(),)
        page_list.append(nex)
        page_str = "".join(page_list)
        return page_str
```

