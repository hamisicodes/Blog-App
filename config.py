import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hamisi:hamisi@localhost/blog'
    SECRET_KEY = 'hamisi'



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hamisi:hamisi@localhost/blog_test'

class DevConfig(Config):
    DEBUG = True
    


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
