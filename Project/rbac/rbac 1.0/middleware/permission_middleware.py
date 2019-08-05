from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import redirect,HttpResponse
import re


class PermissonMiddleware(MiddlewareMixin):
    """权限中间件"""

    def process_request(self, request):

        # 获取当前请求的url
        current_url = request.path_info

        # 白名单检验
        for i in settings.VALID_URL:
            res = re.match(i, current_url)
            if res:
                return None

        # 获取当前session中的所有权限
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)

        if not permission_list:

            return redirect("/login/")

        # 权限校验
        flage = False
        for item in permission_list:

            reg = item.get("permissions__url")
            reg = "^{}$".format(reg)
            if re.match(reg, current_url):
                flage = True
                break

        if not flage:

            return HttpResponse("无权访问....")

