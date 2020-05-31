from flask import request, g
from application import app
from common.models.user import User
from common.lib.password_util import PasswordUtil


@app.before_request
def before_request():
    app.logger.info("===before_request===")
    user_info = check_login()
    g.current_user = None
    if user_info:
        g.current_user = user_info
    return


@app.after_request
def after_request(response):
    app.logger.info("===after_request===")
    return response


def check_login():
    cookies = request.cookies
    cookie_name = app.config['AUTH_COOKIE_NAME']
    auth_cookie = cookies[cookie_name] if cookie_name in cookies else ''

    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        user = User.query.filter_by(id=auth_info[1]).first()
    except Exception:
        return False

    if user is None:
        return False

    if PasswordUtil.gen_auth_code(user) != auth_info[0]:
        return True

    return user
