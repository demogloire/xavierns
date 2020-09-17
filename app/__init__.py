import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import app_config
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
login_manager= LoginManager()
bcrypt = Bcrypt()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)
    #wtf_tinymce.init_app(app)
    

    login_manager.login_message = "Veuillez vous connecté"
    login_manager.login_view = "auth.login"
    login_manager.login_message_category ='danger'
    
    from app import models
    
    #Authentification
    from .authentification import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    #La communauté
    from .communaute import communaute as com_blueprint
    app.register_blueprint(com_blueprint)
    
    #La communauté
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)
    
    return app

