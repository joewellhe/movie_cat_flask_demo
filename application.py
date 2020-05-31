from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_apscheduler import APScheduler
import os
app = Flask(__name__)
manager = Manager(app)

app.config.from_pyfile('config/base_setting.py')
if 'ops_config' in os.environ:
    file_path = os.path.join('config', '{}_setting.py'.format(os.environ['ops_config']))
    app.config.from_pyfile(file_path)


app.logger.info("=================")
# 设置ops_config环境变量
# linux export ops_config=local | production | test|
# windows set ops_config=local | production | test|
db = SQLAlchemy(app)
