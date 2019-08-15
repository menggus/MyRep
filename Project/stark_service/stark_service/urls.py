"""stark_service URL Configuration

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
from django.urls import path
from stark.service.stark import site



urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'stark/', site.urls)
]


"""一.
    查看admin.site.urls, 返回的是一个元组 (self.get_urls(), 'admin', self.name), 同时 self.get_urls() 返回的是一个列表
    
    而这个列表包含了admin路由地址:  如主页, 登录, 退出, 更改密码等等, 以及在admin.py中注册的models的自动生成的相应的增删改查url地址
    
    那么我们是否可以也根据上述返回一个包含 (应用的增删改查url, string, 应用名)的元组来给应用做路由分发呢?
    
    答案是肯定的, 那该什么时候生成以及怎么去生成应用的url以及对应的增删改查视图呢?
    
    url是什么时候生成的?  答案: 服务器启动服务之前就生成了.服务器启动后是不需要做相应的url改变的,即url地址已经固定.
    
    怎样在django中在服务器启动之前就执行响应的代码生成url?   参考admin  autodicover_modules() 方法.    
"""