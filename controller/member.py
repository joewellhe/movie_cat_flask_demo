from flask import Blueprint, render_template
from flask import request, session, make_response, redirect
from flask import jsonify
from common.lib.helper import render_json, render_error, render_html
from common.models.user import User
from common.lib.password_util import PasswordUtil
from application import db, app
from common.lib.url_manger import UrlManager

member = Blueprint("member_page", __name__)


@member.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        return render_html("/member/reg.html")

    req = request.values
    login_name = req['log_name'] if 'log_name' in req else ""
    login_pwd = req['log_pwd'] if 'log_pwd' in req else ""
    re_pwd = req['re_pwd'] if 're_pwd' in req else ""

    if len(login_name) < 5:
        return render_error("用户名需长于5个字符")

    if len(login_pwd) < 6:
        return render_error("请输入正确的密码, 不得短于6个字符")

    if login_pwd != re_pwd:
        return render_error("两次密码不一致")

    user_info = User.query.filter_by(login_name=login_name).first()

    if user_info:
        return render_error("用户名已被注册,请更换~")

    now_user = User()
    now_user.login_name = login_name
    now_user.nickname = login_name
    now_user.login_salt = PasswordUtil.gen_salt()
    now_user.login_pwd = PasswordUtil.gen_password(login_pwd, now_user.login_salt)
    now_user.created_time = UrlManager.get_current_time()
    db.session.add(now_user)
    db.session.commit()
    return render_json(code=200, msg="注册成功", data={})


@member.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_html("/member/login.html")

    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ""
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ""

    if login_name is None or len(login_name) < 6:
        return render_error("请输入正确的用户名和密码")

    now_user = User.query.filter_by(login_name=login_name).first()
    if now_user is None:
        return render_error("当前用户不存在")

    if now_user.login_pwd != PasswordUtil.gen_password(login_pwd, now_user.login_salt):
        return render_error("请输入正确的用户名和密码")

    # session['user'] = now_user.login_name
    response = make_response(render_json(msg="登陆成功"))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],
                        "%s#%s" % (PasswordUtil.gen_auth_code(user=now_user), now_user.id), 60*60*24*7)

    return response


@member.route("/logout")
def logout():
    response = make_response(redirect(UrlManager.build_url('/index')))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response
