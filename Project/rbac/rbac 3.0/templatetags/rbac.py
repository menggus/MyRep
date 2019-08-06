from django.template import Library
from django.conf import settings
from collections import OrderedDict


register = Library()

@register.inclusion_tag('rbac/menu.html')
def menu(request):
    """
        通过执行下面函数menu获取返回结果,并通过装饰器注册到menu.html模板中, 模板就可以获取到menu函数返回的数据
    :param request:
    :return:
    """
    menu_dict = request.session.get(settings.MENU_SESSION_KEY)
    # 对菜单数据进行排序,让显示的菜单一直有序
    order_dict = OrderedDict()
    for key in sorted(menu_dict.keys()):
        order_dict[key] = menu_dict[key]

        # 子菜单默认隐藏
        order_dict[key]["class"] = "hide"

        for item in order_dict[key]['children']:
            if item.get('id') == request.current_id:
                # 控制子菜单是否选中, 以及子菜单是否展示
                item["class"] = "active"
                order_dict[key]["class"] = ""

    return {"menu_dict": order_dict}


@register.inclusion_tag('rbac/breadcrumb.html')
def breadcrumb(request):
    """
        自定义模板标签--- 层级菜单的显示
    :param request:
    :return: 层级菜单的列表
    """
    return {"breadcrumb_list": request.breadcrumb_list}


@register.filter
def has_permission(request, name):

    permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)

    if name in permission_list:

        return True
