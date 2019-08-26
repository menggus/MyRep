"""crm_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from stark.service.stark import site
from django.conf.urls import url

# 问题: 使用path做路由分发时, 所有通过item.pattern.regex.pattern获取的路由分发前缀后面会加上"\/",导致最后生产的url出现"\",
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('stark/', site.urls),
#     path('rbac/', include(("rbac.urls", 'rbac'), namespace='rbac')),  # django 2.0 需要这么写, 不然会报错
#     path('', include(("crm.urls", 'crm'), namespace='crm'))
# ]


urlpatterns = [
    url('admin/', admin.site.urls),
    url('stark/', site.urls),
    url('rbac/', include(("rbac.urls", 'rbac'), namespace='rbac')),  # django 2.0 需要这么写, 不然会报错
    url('', include(("crm.urls", "crm"), namespace='crm')),
]