import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import app_config

db = SQLAlchemy()
login_manager= LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)

    migrate = Migrate(app, db)
    
    from .authentification import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app

from . import models