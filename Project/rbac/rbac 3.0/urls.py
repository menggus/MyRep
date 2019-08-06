from django.conf.urls import url

from rbac.views import permissions_manager

urlpatterns = [

    url(r"^roles/list/$", permissions_manager.roles, name="roles_list"),
    url(r"^roles/add/$", permissions_manager.roles_add, name="roles_add"),
    url(r"^roles/edit/(?P<uid>\d+)/$", permissions_manager.roles_edit, name="roles_edit"),
    url(r"^roles/delete/(?P<uid>\d+)/$", permissions_manager.roles_delete, name="roles_delete"),

    url(r"^menu/list/$", permissions_manager.menu_list, name="menu_list"),
    url(r"^menu/add/$", permissions_manager.menu_add, name="menu_add"),
    url(r"^menu/edit/(?P<mid>\d+)/$", permissions_manager.menu_edit, name="menu_edit"),
    url(r"^menu/delete/(?P<mid>\d+)/$", permissions_manager.menu_delete, name="menu_delete"),

]
