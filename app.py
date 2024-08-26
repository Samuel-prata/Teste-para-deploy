
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

bd = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    from config import Config
    app.config.from_object(Config)

    bd.init_app(app)
    with app.app_context():
        bd.create_all()

    from auth.login import auth as a
    from produtos.routes import produto as p
    app.register_blueprint(p)
    app.register_blueprint(a, url_prefix='/auth')

    return app
