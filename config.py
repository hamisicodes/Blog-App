class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hamisi:hamisi@localhost/blog'
    SECRET_KEY = 'hamisi'



class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
