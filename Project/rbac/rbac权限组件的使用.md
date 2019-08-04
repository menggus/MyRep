### rbac权限组件的使用
 1. 拷贝rbac组件app至项目文件夹

2. rbac组件 - 注册

   ```python
   # settings
   # 注册rbac权限组件
   INSTALLED_APPS = [
       'rbac.apps.RbacConfig'
   ]
   ```

3. rbac权限组件 -  权限校验中间件  注册

   ```python
   # settings
   # 注册rbac组件权限校验中间件
   MIDDLEWARE = [
       'rbac.middleware.permission_middleware.PermissonMiddleware',
   ]
   ```

4. 初始化权限组件数据库

   ```shell
   # 初始化(初始化前清空migrate文件)
   python manager.py makemigrations
   python manager.py migrate
   ```

5. 功能编写,admin后台,添加权限,角色,并给用户赋予权限

   ```markdown
   # 网站后台操作
   ```

6. 配置文件,以及白名单

   ```python
   # settings
   # 权限存储于session  key
   PERMISSION_SESSION_KEY = "Permission"
   MENU_SESSION_KEY = "menu_list"
   VALID_URL = [
       "^/login/$",
       "^/admin/.*$",  # 匹配所有/admin/开头地址
   ]
   ```

7. 登录视图, 通过init_permission初始化权限,写入session

   ```Python
   # 视图中调用即可
   ```

   

8. 动态菜单显示

   ```html
   {# 动态菜单页面 #}
   
   {# 引入动态菜单css #}
   {% load staticfiles %}    {# 顶部引入 #}
   <head>
       	<link rel="stylesheet" href="{% static 'rbac/rbac_menu.css' %} "/>
   </head>
   
   {# 引入动态菜单 #}
   {% load rbac %}  {# 顶部引入 #}
   {% menu request %}
   ```