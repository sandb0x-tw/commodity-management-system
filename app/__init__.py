import json

from flask import Flask
from sqlalchemy import create_engine

from .controllers import user_bp, admin_bp, admin_api_bp
from .models import Base
from .repositories import ProductRepository, TagRepository, ImageRepository
from .services import AuthenticateService

def create_app(config_name):
    # Flask app Initialization
    app = Flask(__name__, template_folder='views')
    app.config.from_object(f"config.{config_name.capitalize()}Config")
    app.jinja_env.variable_start_string = '[['
    app.jinja_env.variable_end_string = ']]'

    # DB Initialization
    app.sql_engine = create_engine(
            f"mysql+pymysql://{app.config.get('DB_USER')}:{app.config.get('DB_PASSWORD')}"
            f"@{app.config.get('DB_HOST')}/{app.config.get('DB_NAME')}"
    )
    Base.metadata.create_all(app.sql_engine)

    # Repository Initialization
    app.product_repository = ProductRepository(app.sql_engine)
    app.tag_repository = TagRepository(app.sql_engine)
    app.image_repository = ImageRepository(app.sql_engine)

    # Services Initializatio
    app.authenticate_service = AuthenticateService(app.config.get('JWT_SECRET'))

    # Blueprints Registration
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(admin_api_bp, url_prefix="/api")

    # Others Initialization
    with open('./data/config.json', 'r', encoding='utf-8') as f:
        app.json_config = json.loads(f.read())
    return app
