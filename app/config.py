import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQL_HOST = "dyud5fa2qycz1o3v.cbetxkdyhwsb.us-east-1.rds.amazonaws.com"
SQL_PORT = "3306"
SQL_USERNAME = "frckdq80jtcrhe01"
SQL_PASSWORD = "w2wlr0b87yq3rvox"
SQL_DATABASE_NAME = "refkiyyw8og41pag" 

class Config(object):
    # url = "mysql:///root:[1234]@[HOST]:[PORT]/[DB_NAME]"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app2.db')
    
    SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}:{}/{}".format(SQL_USERNAME,SQL_PASSWORD,SQL_HOST,SQL_PORT,SQL_DATABASE_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    KAFKA_SERVER = "localhost:9092"
    TOPIC_NAME = "message-to-send"