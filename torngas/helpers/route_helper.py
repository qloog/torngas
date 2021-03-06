#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
from torngas import exception
from tornado.web import url as urlspec
from tornado.util import import_object


class RouteLoader(object):
    """
    路由加载器，将路由加载进tornado的路由系统中
    path:由于设计为子应用形式，路由最终路径为 /path/你的路由，比如blog应用下的/index,会被解析为/blog/index,
        如果不希望在路由前加/path，则为单个路由设置path='/'，path为必填参数
    subapp_name:设置为子应用的模块名，大小写必须相同，必填
    """

    def __init__(self, path=None):
        if not path:
            raise exception.UrlError('path arg not found!')
        self.path = path if path != '/' else ''

    def urlhelper(self, prefix='', *urllist):
        """
        路由列表list
        """
        urls = []
        for u in urllist:
            handler = u.get('handler', '')
            if isinstance(handler, basestring):
                handler_module = '.'.join([prefix, u.get('handler', '')])
                handler_module = import_object(handler_module)
            else:
                handler_module = handler
            pattern = u.get('pattern')
            # pattern += '?' if pattern.endswith('/') else '/?'
            path = u.get('path', None)

            if path:
                if path != '/':
                    pattern = path + pattern
            else:
                pattern = self.path + pattern

            kw = dict(u.get('kwargs', {}))
            # url_name = ''.join([self.subapp_name, '-', u.get('name')])
            url = urlspec(pattern, handler_module, kwargs=kw, name=u.get('name'))
            urls.append(url)

        return urls


class Url(object):
    """

    :param name:路由的名字，设计为必填项。这样能更好的管理路由，方便使用reverse_url生成路由
    :param pattern:路由表达式
    :param view:路由的handler，可为字符串或者view class
    :param kwargs:额外参数提供
    :param path:path:由于设计为子应用形式，路由最终路径为 /path/你的路由，比如blog应用下的/index,会被解析为/blog/index,
        如果不希望在路由前加/path，则为单个路由设置path='/'，path为必填参数
    :return:dict，路由字典
    """

    def __call__(self, name=None, pattern=None, handler='', path=None, kwargs=None):

        if not name:
            raise exception.ArgumentError('You must give a value for "name"')
        if not kwargs:
            kwargs = {}
        if not handler:
            raise exception.ArgumentError('You must give a value for "handler"')

        return dict(
            pattern=pattern,
            handler=handler,
            name=name,
            path=path,
            kwargs=kwargs
        )


url = Url()

