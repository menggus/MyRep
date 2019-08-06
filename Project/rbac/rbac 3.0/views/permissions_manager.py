from django.shortcuts import render, redirect, reverse, HttpResponse
from django import forms
from rbac.models import Role, Menu
from django.utils.safestring import mark_safe


# 角色部分
class RoleForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = "__all__"
        # 给自动生成的标签添加属性
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "permissions": forms.SelectMultiple(attrs={"class": "form-control"})
        }
        # 修改显示字段名
        labels = {
            "permissions": "权限类别",
        }
        # 错误信息自定义
        error_messages = {
            "title": {"required": "角色名不能为空..."}
        }


def roles(request):
    """
        角色列表
    :param request:
    :return:
    """
    if request.method == "GET":

        roles_obj = Role.objects.all()

    return render(request, "rbac/roles_list.html", {"data_list": roles_obj})


def roles_add(request):
    """
        添加角色
    :param request:
    :return:
    """
    if request.method == "GET":

        roleform = RoleForm()

        return render(request, "rbac/roles_add.html", {"form": roleform})

    if request.method == "POST":

        roleform = RoleForm(request.POST)

        if roleform.is_valid():
            roleform.save()

            return redirect(reverse('roles_list'))

        return render(request, "rbac/roles_add.html", {"form": roleform})


def roles_edit(request, uid):
    """
        编辑角色
    :param request:
    :param uid:
    :return:
    """
    role = Role.objects.filter(id=uid).first()
    if not role:

        return HttpResponse("角色不存在.......")

    if request.method == "GET":

        roleform = RoleForm(instance=role)

        return render(request, 'rbac/roles_edit.html', {"form": roleform})

    if request.method == "POST":

        roleform = RoleForm(data=request.POST, instance=role)

        if roleform.is_valid():
            roleform.save()

        return redirect(reverse('roles_list'))


def roles_delete(request, uid):

    role = Role.objects.filter(id=uid).first()

    if not role:

        return HttpResponse("角色不存在")

    role.delete()

    return redirect(reverse("roles_list"))


# 菜单部分
ICON_LIST = [
    ['fa-address-book', '<i aria-hidden="true" class="fa fa-address-book"></i>'],
    ['fa-address-book-o', '<i aria-hidden="true" class="fa fa-address-book-o"></i>'],
    ['fa-address-card', '<i aria-hidden="true" class="fa fa-address-card"></i>'],
    ['fa-address-card-o', '<i aria-hidden="true" class="fa fa-address-card-o"></i>'],
    ['fa-adjust', '<i aria-hidden="true" class="fa fa-adjust"></i>'],
    ['fa-american-sign-language-interpreting',
     '<i aria-hidden="true" class="fa fa-american-sign-language-interpreting"></i>'],
    ['fa-anchor', '<i aria-hidden="true" class="fa fa-anchor"></i>'],
    ['fa-archive', '<i aria-hidden="true" class="fa fa-archive"></i>'],
    ['fa-area-chart', '<i aria-hidden="true" class="fa fa-area-chart"></i>'],
    ['fa-arrows', '<i aria-hidden="true" class="fa fa-arrows"></i>'],
    ['fa-arrows-h', '<i aria-hidden="true" class="fa fa-arrows-h"></i>'],
    ['fa-arrows-v', '<i aria-hidden="true" class="fa fa-arrows-v"></i>']
]
for item in ICON_LIST:
    item[1] = mark_safe(item[1])


def menu_list(request):
    """
        菜单管理
    :param request:
    :return:
    """
    if request.method == "GET":
        menu_objs = Menu.objects.all()

        return render(request, "rbac/menu_list.html", {"data_list": menu_objs})


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = "__all__"
        # 给自动生成的标签添加属性
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "请输入菜单名", "class": "form-control"}),
            "icon": forms.RadioSelect(choices=ICON_LIST)
        }
        error_messages = {
            "title": {
                "required": "菜单标题不能为空",

            },
            "icon": {
                "required": "菜单图标不能为空"
            }
        }


def menu_add(request):

    if request.method == "GET":

        menuform = MenuForm()

    else:
        menuform = MenuForm(request.POST)

        if menuform.is_valid():

            menuform.save()

        return redirect(reverse("menu_list"))

    return render(request, "rbac/menu_add.html", {"form": menuform})


def menu_edit(request, mid):

    menu_obj = Menu.objects.filter(id=mid).first()

    if not menu_obj:

        return HttpResponse("菜单不存在")

    if request.method == "GET":

        menuform = MenuForm(instance=menu_obj)

    else:
        menuform = MenuForm(request.POST)

        if menuform.is_valid():

            menuform.save()

            return redirect(reverse("menu_list"))

    return render(request, "rbac/menu_add.html", {"form": menuform})


def menu_delete(request, mid):

    menu_obj = Menu.objects.filter(id=mid).first()

    if not menu_obj:
        return HttpResponse("菜单不存在")

    menu_obj.delete()

    return redirect(reverse("menu_list"))
