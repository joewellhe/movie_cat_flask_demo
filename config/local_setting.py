# 本地环境配置
from config.base_setting import *
from common.lib.url_manger import UrlManager

# DEBUG = False
# SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/movie_cat"
SECRET_KEY = 'joe'
STATIC_RELEASE = '20200518'
AUTH_COOKIE_NAME = 'login_cache'
