from flask import Flask, render_template
from config import Config
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config[config_name])
    Config[config_name].init_app(app)
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
    return app