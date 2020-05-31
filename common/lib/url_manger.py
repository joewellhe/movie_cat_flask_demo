# -*- coding: utf-8 -*-
import datetime
from application import app


def get_release():
    if app.config['DEBUG']:
        return UrlManager.get_current_time()
    else:
        return app.config['STATIC_RELEASE']


class UrlManager(object):
    @staticmethod
    def build_url(path):
        config_domain = app.config['DOMAIN']
        return '%s%s' % (config_domain['www'], path)

    @staticmethod
    def build_static_url(path):
        path = "/static" + path + '?ver=' + get_release()
        return UrlManager.build_url(path)

    @staticmethod
    def get_current_time(fmt='%Y%m%d%H%M%S'):
        time = datetime.datetime.now()
        return time.strftime(fmt)
