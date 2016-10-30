# -*- coding:utf-8 -*-
from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object("config")
# 注册数据库
db = MongoEngine()
app.config['MONGODB_SETTINGS'] = {'db': 'rundb'}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
db.init_app(app)
# 管理员蓝本
from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint)
