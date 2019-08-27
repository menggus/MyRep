#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf import settings
from django.utils.module_loading import import_string
from django.urls import URLResolver
from collections import OrderedDict


def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):
    """
        递归获取路由系统中的所有url
    :param pre_namespace:
    :param pre_url:
    :param urlpatterns:
    :param url_ordered_dict:
    :return:
    """
    for item in urlpatterns:
        # 判断是否是路由分发类,即项目下的urls.py
        if isinstance(item, URLResolver):

            if pre_namespace:
                if item.namespace:
                    namespace = "%s:%s" % (pre_namespace, item.namespace,)
                else:
                    namespace = pre_namespace
            else:

                if item.namespace:
                    namespace = item.namespace

                else:
                    namespace = None

            # 问题: 所有通过item.pattern.regex.pattern获取的路由分发前缀后面会加上"\/",导致最后生产的url出现"\",
            # 例如:/stark\/crm/department/list/
            # 此问题出现 是项目主ulr下采用的是path()来做路由分发出现, 如果采用url来不会出现上述问题
            # if r"\/" in patt:
            #     patt = patt.replace(r"\/", "/")  # 通过
            #     # patt = patt.split(r'\/')[0] + "/"  # 通过
            # print(patt)
            patt = item.pattern.regex.pattern
            recursion_urls(namespace, pre_url + patt, item.url_patterns, url_ordered_dict)
        else:
            # 根路由, 应用下的urls.py
            if pre_namespace:
                name = "%s:%s" % (pre_namespace, item.name,)
            else:
                name = item.name

            if not item.name:
                raise Exception('URL路由中必须设置name属性')

            patt = item.pattern.regex.pattern

            url = pre_url + patt

            url_ordered_dict[name] = {'name': name, 'url': url.replace('^', '').replace('$', '')}


def get_all_url_dict(ignore_namespace_list=None):
    """
    获取路由中
    :return:
    """
    ignore_list = ignore_namespace_list or []
    url_ordered_dict = OrderedDict()

    md = import_string(settings.ROOT_URLCONF)
    # print(md.urlpatterns)
    urlpatterns = []

    for item in md.urlpatterns:

        if item.namespace in ignore_list:
            continue
        urlpatterns.append(item)

    recursion_urls(None, "/", urlpatterns, url_ordered_dict)

    print(url_ordered_dict)

    return url_ordered_dict

