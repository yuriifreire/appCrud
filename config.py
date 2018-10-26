# config.py

class Config(object):
    """
    Config comum
    """



class DevelopmentConfig(Config):
    """
    Config desenvolvimento
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Config producao
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}