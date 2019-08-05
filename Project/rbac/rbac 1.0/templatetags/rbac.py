from django.template import Library
from django.conf import settings
import re

register = Library()

# 通过执行下面函数menu获取返回结果,并通过装饰器注册到menu.html模板中, 模板就可以获取到menu函数返回的数据
@register.inclusion_tag('rbac/menu.html')
def menu(request):

    menu_list = request.session.get(settings.MENU_SESSION_KEY)

    current_url = request.path_info

    for item in menu_list:

        reg = "^{}$".format(item.get('url'))

        if re.match(reg, current_url):
            item["class"] = "active"

    return {"menu_list": menu_list}
