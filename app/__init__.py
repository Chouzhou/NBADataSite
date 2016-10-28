# -*- coding:utf-8 -*-
from flask import Flask, render_template
from config import Config
from flask_mongoengine import MongoEngine


db = MongoEngine()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config[config_name])
    #db = MongoEngine(app)
    Config[config_name].init_app(app)
    # 注册数据库
    app.config['MONGODB_SETTINGS'] = {'db': 'rundb'}
    db.init_app(app)
    # 管理员蓝本
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
    return app
