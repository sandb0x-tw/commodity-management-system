from flask import Flask

from sqlalchemy import create_engine

from .controllers import user_bp, admin_bp, admin_api_bp
from .models import Base

def create_app(config_name):
    app = Flask(__name__, template_folder='views')

    app.config.from_object(f"config.{config_name.capitalize()}Config")

    # DB Initialization
    app.sql_engine = create_engine(
            f"mysql+pymysql://{app.config.get('DB_USER')}:{app.config.get('DB_PASSWORD')}"
            f"@{app.config.get('DB_HOST')}/{app.config.get('DB_NAME')}"
    )
    Base.metadata.create_all(app.sql_engine)

    # Blueprints Registration
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(admin_api_bp, url_prefix="/api")

    return app
