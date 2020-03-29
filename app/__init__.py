from flask import Flask, escape, request
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
 

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)

from app.models import user,company

user = user.User
company = company.Company

migrate = Migrate(app, db)

from app import routes




 