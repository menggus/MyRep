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
        permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)

        if not permission_dict:

            return redirect("/login/")

        # 层级菜单列表
        request.breadcrumb_list = [
            {"title": "首页", "url": "/"}
        ]

        # 权限校验
        flage = False

        for item in permission_dict.values():

            pname = item.get('pname')
            pid = item.get('pid')
            reg = item.get("url")
            reg = "^{}$".format(reg)

            print(reg, current_url)

            if re.match(reg, current_url):
                flage = True

                # 引入一个current_id 为了在rbac.py中,把当前的权限与菜单进行关联,当点击某功能时,显示对应的菜单
                if pid:
                    request.current_id = item.get('pid')

                    request.breadcrumb_list.extend([
                        {"title": permission_dict[pname].get('title'), "url": permission_dict[pname].get('url')},
                        {"title": item.get('title'), "url": item.get('url')},
                    ])


                else:
                    request.current_id = item.get('id')
                    request.breadcrumb_list.extend([
                        {"title": item.get('title'), "url": item.get('url')},
                    ])

                break

        if not flage:

            return HttpResponse("无权访问....")

