from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_babel import Babel
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()
babel = Babel()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    babel.init_app(app)

    # Blueprints
    from app.routes.auth import auth_bp
    from app.routes.book import book_bp
    from app.routes.library import library_bp
    from app.routes.borrow import borrow_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(book_bp, url_prefix='/api/books')
    app.register_blueprint(library_bp, url_prefix='/api/libraries')
    app.register_blueprint(borrow_bp, url_prefix='/api')

    return app

@babel.localeselector
def get_locale():
    from flask import request
    return request.accept_languages.best_match(['en', 'hi', 'te'])
