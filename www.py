from application import app
from controller.index import index_page
from controller.member import member

# from flask_debugtoolbar import DebugToolbarExtension


@app.route('/')
def hello():
    return "I love Flask"


'请求拦截 错误处理'
from intercentors.auth import *
from intercentors.error import *

# toolbar = DebugToolbarExtension(app)
app.register_blueprint(index_page, url_prefix='/')
app.register_blueprint(member, url_prefix='/user')


'''函数模板'''
from common.lib.url_manger import UrlManager
app.add_template_global(UrlManager.build_static_url, 'build_static_url')
app.add_template_global(UrlManager.build_url, 'build_url')
