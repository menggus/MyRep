from django.conf.urls import url
from django.shortcuts import HttpResponse


class StarkConfig(object):
    def __init__(self, model_class, site):
        self.model_class = model_class
        self.site = site

    def func(self):
        print(self.model_class)

    def run(self):
        self.func()

    def changelist_view(self, request):
        print(self.model_class)

        return HttpResponse('...')

    def add_view(self,request):
        pass

    def change_view(self,request,pk):
        pass

    def delete_view(self,request,pk):
        pass

    def get_urls(self):
        info = self.model_class._meta.app_label, self.model_class._meta.model_name

        urlpatterns = [
             url(r'^list/$', self.changelist_view,name='%s_%s_changelist' %info),
             url(r'^add/$', self.add_view,name='%s_%s_add' %info),
             url(r'^(?P<pk>\d+)/change/', self.change_view, name='%s_%s_change' %info),
             url(r'^(?P<pk>\d+)/del/', self.delete_view, name='%s_%s_del' %info),
        ]

        extra = self.extra_url()
        if extra:
            urlpatterns.extend(extra)

        return urlpatterns

    def extra_url(self):
        pass

    @property
    def urls(self):
        return self.get_urls()


class AdminSite(object):
    def __init__(self):
        self._registry = {}
        self.app_name = 'stark'
        self.namespace = 'stark'

    def register(self, model_class, stark_config=None):
        # model_class＝models.Role
        # stark_config=None
        if not stark_config:
            stark_config = StarkConfig
        # model_class＝models.Role
        # stark_config=RoleConfig
        self._registry[model_class] = stark_config(model_class,self)
        """
        {
            models.UserInfo: StarkConfig(models.UserInfo), # 封装：model_class=UserInfo，site=site对象
            models.Role: RoleConfig(models.Role)           # 封装：model_class=Role，site=site对象
        }
        """

    def get_urls(self):

        urlpatterns = []
        # urlpatterns.append(url(r'^x1/', self.x1))
        # urlpatterns.append(url(r'^x2/', self.x2))
        # urlpatterns.append(url(r'^x3/', ([
        #                                      url(r'^add/', self.x1),
        #                                      url(r'^change/', self.x1),
        #                                      url(r'^del/', self.x1),
        #                                      url(r'^edit/', self.x1),
        #                                  ],None,None)))

        for k, v in self._registry.items():
            # k=modes.UserInfo,v=StarkConfig(models.UserInfo), # 封装：model_class=UserInfo，site=site对象
            # k=modes.Role,v=RoleConfig(models.Role)           # 封装：model_class=Role，site=site对象
            app_label = k._meta.app_label
            model_name = k._meta.model_name
            urlpatterns.append(url(r'^%s/%s/' %(app_label,model_name,), (v.urls,None,None)))
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.namespace

site = AdminSite()

















