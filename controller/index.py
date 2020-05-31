from flask import Blueprint, request, make_response, jsonify, render_template, session
from common.models.user import User
from sqlalchemy import text
from common.lib.helper import render_html

index_page = Blueprint('index_page', __name__)



@index_page.route('/get')
def get():
    # var_a = request.args.get("a", "I love benben")
    req = request.values
    var_a = req['a'] if 'a' in req else 'I love Flask get'
    return "request: {} ==== paras: {} ==== var_a: {}".format(request.method, request.args, var_a)


@index_page.route("/post", methods=['post'])
def post():
    # var_a = request.form['a'] if 'a' in request.form else ''
    req = request.values
    var_a = req['a'] if 'a' in req else 'I love Flask post'
    return "request: {} ==== args:{} ==== paras: {} ==== var_a: {}".format(request.method, request.args, request.form, var_a)


@index_page.route('/upload', methods=['post'])
def upload():
    f = request.files['file']
    return "request: {} ==== paras: {} ==== f: {}".format(request.method, request.files, f)


# @index_page.route('/text')
# def text():
#     response = make_response("text/html", 404)
#     return response


@index_page.route('/json')
def myjson():
    s = {'a': 'b'}
    # response = make_response(json.dumps(s))
    # response.headers['Content-Type'] = 'application/json'
    response = make_response(jsonify(s))
    return response


@index_page.route('/index')
def myhtml():
    context = {'name': 'jinyao'}
    context['user'] = {'nickname': 'wujinyao',
                       'qq': '123123123'}
    context['numlist'] = [1, 2, 3, 4, 5]

    # sql = text("select * from user ")
    # result = db.engine.execute(sql)
    result = User.query.all()
    context['result'] = result
    # print(session['user'])
    # from flask import g
    # print("==================")
    # print(g.current_user.nickname)
    return render_html('index.html', context)
    # return render_template('index.html', **context)


@index_page.route('/extent_1')
def extend():
    return render_template('entext_1.html')


@index_page.route('/extent_2')
def extend1():
    return render_template('entext_2.html')
