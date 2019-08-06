# 查询出来的结果data
data = [
    {'permissions__menu__title': '信息管理', 'permissions__menu_id': 1, 'permissions__title': '客户列表', 'permissions__menu__icon': 'fa-address-book', 'permissions__url': '/customer/list/'},
    {'permissions__menu__title': '信息管理', 'permissions__menu_id': 1, 'permissions__title': '账单列表', 'permissions__menu__icon': 'fa-address-book', 'permissions__url': '/payment/list/'},
    {'permissions__menu__title': None, 'permissions__menu_id': None, 'permissions__title': '添加客户', 'permissions__menu__icon': None, 'permissions__url': '/customer/add/'}
]

menu_dict = {}

for item in data:
    menu_id = item.get("permissions__menu_id")

    if not menu_id:
        continue

    if menu_id not in menu_dict:
        menu_dict[menu_id] = {
            "title": item.get("permissions__menu__title"),
            "icon": item.get("permissions__menu__icon"),
            "children": [
                {"title": item.get("permissions__title"), "url": item.get("permissions__url")}
            ]
        }
    else:
        menu_dict[menu_id]["children"].append(
            {"title": item.get("permissions__title"), "url": item.get("permissions__url")}
        )

print(menu_dict)