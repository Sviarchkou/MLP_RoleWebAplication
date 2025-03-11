import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lab1.db'
    SECRET_KEY = os.urandom(32)
    JWT_SECRET_KEY = 'so-damn-secret-key'
    JWT_TOKEN_LOCATION = 'cookies'
    WTF_CSRF_ENABLED = True
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_CSRF_CHECK_FORM = True