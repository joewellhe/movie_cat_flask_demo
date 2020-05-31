from flask import jsonify, render_template, g


def render_html(template, context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template, **context)


def render_json(code=200, msg='操作成功', data={}):
    res = {"code": code,
           "msg": msg,
           "data": data}
    return jsonify(res)


def render_error(msg="操作失败"):
    return render_json(code=-1, msg=msg, data={})
