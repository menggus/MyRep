from stark.service.stark import site, StarkConfig
from .models import Role
from django.conf.urls import url
from django.shortcuts import HttpResponse


class RoleConfig(StarkConfig):
    """
        用于自定义模型生成url配置
    """
    def extra_url(self):
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        urlpatterns = [
            url(r"^replace/$", self.replace, name="%s_%s_replace" % info)
        ]

        return urlpatterns

    def replace(self, request):

        return HttpResponse("replace")


site.registry(Role, RoleConfig)