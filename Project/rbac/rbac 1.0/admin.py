from django.contrib import admin

# Register your models here.
from .models import Role, UserInfo, Permission


class PermissionAdmin(admin.ModelAdmin):
    """主站点,显示"""
    list_display = ("title", "url")
    list_editable = ("url",)


admin.site.register(Role)
admin.site.register(UserInfo)
admin.site.register(Permission, PermissionAdmin)