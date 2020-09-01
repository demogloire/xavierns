class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = '9462bfc3ca8d37b136173798873d05ea'


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    SECRET_KEY = '9462bfc3ca8d37b136173798873d05ea'

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}