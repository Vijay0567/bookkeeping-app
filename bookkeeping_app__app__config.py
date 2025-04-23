import os

class Config:
    # Secret key for session and JWT
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')
    
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///bookkeeping.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Configuration
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-key')
    
    # Babel Configuration
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_TRANSLATION_DIRECTORIES = 'app/translations'

    # Firebase Configuration
    FIREBASE_STORAGE_BUCKET = os.environ.get('FIREBASE_STORAGE_BUCKET', 'your-firebase-bucket')
    FIREBASE_CREDENTIALS = os.environ.get('FIREBASE_CREDENTIALS', 'firebase_credentials.json')
