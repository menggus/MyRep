from django.contrib import admin

# Register your models here.
from .models import Role, UserInfo, Permission, Menu


class PermissionAdmin(admin.ModelAdmin):
    """主站点,显示"""
    list_display = ("title", "url", "name")
    list_editable = ("url", "name")


admin.site.register(Permission, PermissionAdmin)

admin.site.register(Role)


class UserinfoAdmin(admin.ModelAdmin):
    """显示用户详细情况"""
    list_display = ("name","password", "email", )
    lsit_editable = ("roles",)


admin.site.register(UserInfo, UserinfoAdmin)

admin.site.register(Menu)