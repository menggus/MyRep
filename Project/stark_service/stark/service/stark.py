
"""三.
     怎么样生成应用的url

     需要使用単例模式, 来生成一个实例对象来管理应用模型获取urls;

     需要面向对象编程多态来针对不同的应用实现不同的urls功能

"""
from django.conf.urls import url, include
from django.shortcuts import HttpResponse


class StarkConfig():
    """
        模型类的默认url生成配置
    """
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
            url(r'^list/$', self.changlist_view, name="%s_%s_changlist" % info),
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

        return False

    """定义url相关视图"""
    def changlist_view(self, request):

        return HttpResponse("changlist_view")

    def add_view(self, request):

        return HttpResponse("add_view")

    def change_view(self, request, pk):

        return HttpResponse("change_view")

    def delete_view(self, request, pk):

        return HttpResponse("delete_view")


class AdminSite():
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