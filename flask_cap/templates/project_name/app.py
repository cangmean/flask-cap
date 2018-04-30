"""
应用模块
"""
from flask import Flask

# pylint: disable=all


def create_app():
    """ 创建应用"""
    app = Flask(
        __name__,
    )

    configure_app(app)
    configure_request_hook(app)
    configure_extensions(app)
    configure_blueprints(app)
    return app


def configure_app(app):
    """ 基础配置"""
    from {{ project_name }} import config as config_file
    app.config.from_object(config_file)


def configure_blueprints(app):
    """ 配置蓝图"""
    from {{ project_name }}.api import bp as api_bp
    from {{ project_name }}.views import bp as views_bp
    app.register_blueprint(api_bp)
    app.register_blueprint(views_bp)


def configure_extensions(app):
    """ 配置扩展"""
    from {{ project_name }}.extends import api, db, login_manager
    api.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)


def configure_request_hook(app):
    """ 请求钩子"""

    @app.before_request
    def before_request():
        """ 请求前钩子"""
        pass

    @app.after_request
    def after_request(response):
        """ 请求后钩子"""
        # response.headers['Access-Control-Allow-Origin'] = '*'
        # response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,OPTIONS'
        # response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,token' 
        return response