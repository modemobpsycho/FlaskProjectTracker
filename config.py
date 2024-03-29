import os
from decouple import config
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    FLASK_ENV = "base"
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config("SECRET_KEY", default=os.getenv("SECRET_KEY"))
    DATABASE_URL = config("DATABASE_URL", default=os.getenv("DATABASE_URL"))
    SQLALCHEMY_DATABASE_URI = config(
        "SQLALCHEMY_DATABASE_URI", default=os.getenv("SQLALCHEMY_DATABASE_URI")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 10
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SECURITY_PASSWORD_SALT = config("SECURITY_PASSWORD_SALT", default="very-important")

    MAIL_DEFAULT_SENDER = config("MAIL_DEFAULT_SENDER", default="MAIL_DEFAULT_SENDER")
    MAIL_SERVER = "smtp.mail.ru"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = False
    MAIL_USERNAME = config("MAIL_USERNAME", default="MAIL_USERNAME")
    MAIL_PASSWORD = config("MAIL_PASSWORD", default="MAIL_PASSWORD")
    FLASK_DOCKER = config("FLASK_DOCKER", default=os.getenv("FLASK_DOCKER"))
    UPLOAD_FOLDER = config("UPLOAD_FOLDER", default=os.getenv("UPLOAD_FOLDER"))


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    APP_SETTINGS = "config.DevelopmentConfig"
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = True


class TestingConfig(Config):
    FLASK_ENV = "testing"
    APP_SETTINGS = "config.TestingConfig"
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    FLASK_ENV = "production"
    APP_SETTINGS = "config.ProductionConfig"
    DEBUG = False
    DEBUG_TB_ENABLED = False
