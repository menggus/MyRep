# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from crm.models import UserInfo
from rbac.service import init_permission


def login(request):

    if request.method == "GET":

        return render(request, "login.html")

    user = request.POST.get("user")
    pwd = request.POST.get("password")

    obj = UserInfo.objects.filter(name=user, password=pwd).first()

    if not obj:

        return HttpResponse("登录出错请重新登录....")

    init_permission.init_permission(obj, request)

    # 存入用户信息至session
    request.session["userinfo"] = {"id": obj.id, "name": obj.name}

    return redirect("/rbac/menu/list")