from django.conf import settings


def init_permission(request, user):
    """
        权限初始化;
        登录视图中, 通过调用该方法来获取权限;
    :param request:
    :param user:
    :return:
    """
    # 从数据库查询权限信息
    permission_obj = user.roles.filter(permissions__url__isnull=False).values('permissions__title',
                                                                              'permissions__id',
                                                                              'permissions__name',
                                                                              'permissions__pid',
                                                                              'permissions__url',
                                                                              'permissions__menu_id',
                                                                              'permissions__menu__title',
                                                                              'permissions__menu__icon').distinct()

    # 所有权限列表 和 菜单字典
    permission_dict = {}
    menu_dict = {}

    for item in permission_obj:
        # 获取权限并保存到自定义权限列表permission_list
        permission_dict[item.get('permissions__name')] = {'id': item.get('permissions__id'),
                                                          'url': item.get('permissions__url'),
                                                          'pid': item.get('permissions__pid'),
                                                          'name': item.get('permissions__name'),
                                                          "title": item.get('permissions__title')}

        menu_id = item.get("permissions__menu_id")

        if not menu_id:
            continue

        if menu_id not in menu_dict:
            menu_dict[menu_id] = {
                "title": item.get("permissions__menu__title"),
                "icon": item.get("permissions__menu__icon"),
                "children": [
                    {"id": item.get('permissions__id'),
                     "title": item.get("permissions__title"),
                     "url": item.get("permissions__url")
                     }
                ]
            }
        else:
            menu_dict[menu_id]["children"].append(
                {"id": item.get('permissions__id'),
                 "title": item.get("permissions__title"),
                 "url": item.get("permissions__url")}
            )

    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.MENU_SESSION_KEY] = menu_dict
