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
                                                                              'permissions__url',
                                                                              'permissions__is_menu',
                                                                              'permissions__icon',).distinct()

    # 所有权限列表 和 菜单权限
    permission_list = []
    menu_list = []

    for item in permission_obj:
        # item: {'permissions__is_menu': True, 'permissions__icon': 'fa-bandcamp',
        # 'permissions__url': '/customer/list/', 'permissions__title': '客户列表'}
        # 获取权限并保存到自定义权限列表permission_list
        permission_list.append({'permissions__url': item.get('permissions__url')})

        if item.get('permissions__is_menu'):
            # 保存可做菜单的权限
            menu_list.append({'title': item.get("permissions__title"),
                              'url': item.get("permissions__url"),
                              'icon': item.get("permissions__icon")})

    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.MENU_SESSION_KEY] = menu_list
