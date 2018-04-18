import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
#    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=bhri,pw=bhrisri,url=localhost,db=wordcount_dev)
 #   SQLALCHEMY_DATABASE_URI = DB_URL

    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    POSTGRES = {
    'user': 'bhri',
    'pw': 'bhrisri',
    'db': 'wordcount_dev',
    'host': 'localhost',
    'port': '5432',
     }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
