from stark.service.stark import site, StarkConfig
from .models import Role
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.utils.safestring import mark_safe


class RoleConfig(StarkConfig):
    """
        继承StarkConfig自定义相关配置
        1. 自定义url
        2. 自定义视图函数
        3. 自定义表格第一列 checkbox
    """
    list_display = [StarkConfig.display_checkbox, "id", "name"]


    def extra_url(self):
        """
            1.自定义额外的 url
        :return:
        """
        info = self.model_class._meta.app_label, self.model_class._meta.model_name

        urlpatterns = [
            url(r"^replace/$", self.replace, name="%s_%s_replace" % info)
        ]

        return urlpatterns

    def replace(self, request):
        """
            2. 自定义视图函数
        :param request:
        :return:
        """
        return HttpResponse("replace")

    # def display_checkbox(self, row=None, header=None):
    #     """
    #         3.自定义表格第一列 checkbox
    #         问题: 如果每一个子类都需要这个定制呢? 可以将该功能放到StarkConfig下
    #     :param row:
    #     :param header:
    #     :return:
    #     """
    #     if header:
    #         return "选择"
    #
    #     return mark_safe('<input type="checkbox" name="pk" pk=%s >' % row.pk)



site.registry(Role, RoleConfig)