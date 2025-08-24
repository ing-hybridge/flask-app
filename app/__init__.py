from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializa SQLAlchemy
    db.init_app(app)

    # IMPORTA modelos DESPUÉS de init_app para registrar tablas
    from . import models  # noqa: F401

    # Registra blueprints
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Crea tablas
    with app.app_context():
        db.create_all()

    return app
