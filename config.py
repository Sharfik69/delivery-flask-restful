import local_settings


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True

    SQLALCHEMY_DATABASE_URI = local_settings.__URI_DATABASE__
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = local_settings.__SECRET_KEY__


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
