#-*-coding=utf-8-*-
import os
############
#   中间件  #
############
MIDDLEWARE_CLASSES = (
    'torngas.middleware.session.SessionMiddleware',
    'torngas.middleware.signal.SignalMiddleware',
)

############
# 加载的应用 #
############
INSTALLED_APPS = (

    'helloworld',
)


###########
# 缓存配置 #
###########
CACHES = {
    'default': {
        'BACKEND': 'torngas.cache.backends.localcache.LocMemCache',
        'LOCATION': 'process_cache',
        'OPTIONS': {
            'MAX_ENTRIES': 10000,
            'CULL_FREQUENCY': 3
        }
    },
    'default_memcache': {
        'BACKEND': 'torngas.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '127.0.0.1:11211'
        ],
        'TIMEOUT': 300
    },
    'dummy': {
        'BACKEND': 'torngas.cache.backends.dummy.DummyCache'
    },
    'filebased': {
        'BACKEND': 'torngas.cache.backends.filebased.FileBasedCache',
        'LOCATION': '.'
    },
    'default_redis': {
        'BACKEND': 'torngas.cache.backends.rediscache.RedisCache',
        'LOCATION': '192.168.1.103:6379',
        'TIMEOUT': 300,
        'OPTIONS': {
            'DB': 0,
            # 'PASSWORD': 'yourredispwd',
            'PARSER_CLASS': 'redis.connection.DefaultParser'
        },
        'KEY_PREFIX': '',
        'VERSION': 1
    },

}



#################
#本地化翻译文件地址#
#################
TRANSLATIONS = False  #是否开启国际化
TRANSLATIONS_CONF = {
    'translations_dir': os.path.join(os.path.dirname(__file__), 'translations'),
    'locale_default': 'zh_CN',
    'use_accept_language': True
}

#tornado全局配置
TORNADO_CONF = {
    "static_path": os.path.join(os.path.dirname(__file__), "../static"),
    "xsrf_cookies": True,
    "debug": True,
    "xheaders": True,
    "login_url": '/login',
    "permanent_session_lifetime": 0,
    "cookie_secret": "bXZ/gDAbQA+zaTxdqJwxKa8OZTbuZE/ok3doaow9N4Q=",
    "template_path": os.path.join(os.path.dirname(__file__), "../templates"),
    #安全起见，可以定期生成新的cookie 秘钥，生成方法：
    #base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
}

#白名单未开启，如需使用，请用元祖列出白名单ip
WHITELIST = False
#######
# WHITELIST = (
#     '127.0.0.1',
# '127.0.0.2',
# )

#tornado日志功能配置
LOG_CONFIG = {
    'level': 'info',  #日志级别
    'rotating_handler': 'TimedRotatingFileHandler',  #备份类型，目前默认仅支持使用RotatingFileHandler，或TimedRotatingFileHandler
    'filesize': 1000 * 1000 * 1000,  #日志文件大小限制,针对file方式
    'backup_num': 5,  #最多保留文件数
    # params when:
    # 'S'	Seconds
    # 'M'	Minutes
    # 'H'	Hours
    # 'D'	Days
    # 'W0'-'W6'	Weekday (0=Monday)
    # 'midnight'	Roll over at midnight
    #备份时间类型，默认D
    'when': 'H',
    'interval': 1,
    'delay': True,
    'suffix': '%Y-%m-%d_%H%M%S',
    'log_to_stderr': True
}
#日志logger名，不同的日志名会相应生成不同的日志目录
# {'日志目录名','logger名'}
#使用时通过logging.getLogger(logger名)可以拿到相应的logger
LOG_RELATED_NAME = {
    'exception_log': 'exception',
    'info_log': 'info'
}
IPV4_ONLY = True

#开启session支持
SESSION = {
    'session_cache_alias': 'default',  # 'session_loccache',
    'session_name': '__TORNADOID',
    'cookie_domain': '',
    'cookie_path': '/',
    'expires': 0,  # 24 * 60 * 60, # 24 hours in seconds
    'ignore_change_ip': False,
    # 'expired_message': 'Session expired',
    'httponly': True,
    'secure': False,
    'secret_key': 'fLjUfxqXtfNoIldA0A0J',
    'session_version': 'V1'
}

#配置模版引擎
#引入相应的TemplateLoader即可
#若使用自带的请给予None
#支持mako和jinja2
#mako设置为torngas.template.mako_loader.MakoTemplateLoader
#jinj2设置为torngas.template.jinja2_loader.Jinja2TemplateLoader
#初始化参数请参照jinja的Environment或mako的TemplateLookup,不再详细给出
TEMPLATE_CONFIG = {
    'template_engine': 'torngas.template.jinja2_loader.Jinja2TemplateLoader',

    #模版路径由torngas.handler中commonhandler重写，无需指定，模版将存在于每个应用的根目录下
    'filesystem_checks': True,  #通用选项
    'cache_directory': '../_tmpl_cache',  #模版编译文件目录,通用选项
    'collection_size': 50,  #暂存入内存的模版项，可以提高性能，mako选项,详情见mako文档
    'cache_size': 0,  #类似于mako的collection_size，设定为-1为不清理缓存，0则每次都会重编译模板
    'format_exceptions': False,  #格式化异常输出，mako专用
    'autoescape': False  #默认转义设定，jinja2专用

}

# 用编译的正则表达式来限定user-agent，来自django，可参考django的处理方式
# example:
# import re
# DISALLOWED_USER_AGENTS = (
#     re.compile(r'^NaverBot.*'),
#     re.compile(r'^EmailSiphon.*'),
#     re.compile(r'^SiteSucker.*'),
#     re.compile(r'^sohu-search')
# )
DISALLOWED_USER_AGENTS = ()

#为所有的url移除尾部'/'
REMOVE_SLASH_ALL = True