import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # url = "mysql:///root:[1234]@[HOST]:[PORT]/[DB_NAME]"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app2.db')
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/testesd"
    SQLALCHEMY_TRACK_MODIFICATIONS = False