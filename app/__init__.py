from flask import Flask
from .controllers import user_bp, admin_bp, admin_api_bp

def create_app(config_name):
    app = Flask(__name__, template_folder='views')

    app.config.from_object(f"config.{config_name.capitalize()}Config")

    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(admin_api_bp, url_prefix="/api")

    return app
