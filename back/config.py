from os import environ

class BaseConfig(object):
    """Base configuration."""

    DEBUG = None
    DB_HOST = "bd_name"
    DB_USER = "db_user"
    DB_PASS = "db_pass"
    DB_NAME = "db_name"
    SECRET_KEY = "secret"

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass


class DevelopmentConfig(BaseConfig): #Local de cada uno
    """Development configuration."""

    ENV = "development"
    DEBUG = environ.get("DEBUG", True)
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "root")
    DB_PASS = environ.get("DB_PASS", "root")
    DB_NAME = environ.get("DB_NAME", "deu")


class TestingConfig(BaseConfig): 
    """Testing configuration."""

    ENV = "testing"
    TESTING = True
    DEBUG = environ.get("DEBUG", True)
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "root")
    DB_PASS = environ.get("DB_PASS", "root")
    DB_NAME = environ.get("DB_NAME", "proyectoTest")


class ProductionConfig(BaseConfig): #Configuarion del servidor remoto
    """Production configuration."""

    ENV = "production"
    DEBUG = environ.get("DEBUG", False)
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "grupo8")
    DB_PASS = environ.get("DB_PASS", "NDZjZTg1NzAwYzcy")
    DB_NAME = environ.get("DB_NAME", "grupo8")


config = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)
