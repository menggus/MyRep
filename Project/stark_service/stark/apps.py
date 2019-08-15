from django.apps import AppConfig


class StarkConfig(AppConfig):
    name = 'stark'

    def ready(self):
        from django.utils.module_loading import autodiscover_modules
        """二.
            stark: autodiscover_modules() 方法, 来自于admin源码, 在启动服务器时会发现每个应用中的admin.py并执行,来获取需要来用于
            admin管理的模型类.
            
            应用该原理, 我们用来自动发现我们所创建的stark.py文件, 来获取相应的功能
            
            通过每个应用中的stark.py文件的执行,来生成需要的应用的功能url地址
        
            怎么实现应用的url地址的生成?  stark.py实现
        """
        autodiscover_modules('stark')
