from flask import Flask
from config import Config
from extensions import db
#, migrate)

# from routes.main import main_bp
# from routes.auth import auth_bp
from routes.test import test_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # app.register_blueprint(main_bp)
    # app.register_blueprint(auth_bp)

    app.register_blueprint(test_bp)

    db.init_app(app)
    # migrate.init_app(app, db)
    # login_manager.init_app(app)

    # login_manager.login_view = 'login'
    # login_manager.login_message = 'Вы не можете войти в систему без авторизации'

    with app.app_context():
        db.create_all()

    return app










# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///laba1.db'
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)

#app.register_blueprint(auth, url_prefix='/auth')


#
# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('config.Config')
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///laba1.db'
#
#     db.init_app(app)
#
#     db = SQLAlchemy(app)
#
#
#     #from app.auth.routes import auth_bp
#     #from app.blog.routes import blog_bp
#     #app.register_blueprint(auth_bp, url_prefix='/auth')
#     #app.register_blueprint(blog_bp, url_prefix='/blog')
#
#     return app
