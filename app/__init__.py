import os
from flask import Flask, escape, request
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
 
# os.environ["DATABASE_URL"] = "postgres://klshqakpumicqw:b81648d62aba36df00aac43c2ae849a9e238bf07ca3a266eb956ddfc96f75c8c@ec2-52-86-73-86.compute-1.amazonaws.com:5432/dcjvpvavero43d"

app = Flask(__name__)
app.config.from_object(config.Config)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

from app.models import user,company,client,message,message_client

decodeToken = user.decode_auth_token
user = user.User
company = company.Company
clients = client.Client
messages = message
message_clients = message_client 

migrate = Migrate(app, db)

from app import routes




 