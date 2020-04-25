from flask import Flask, escape, request
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
 

app = Flask(__name__)
app.config.from_object(config.Config)
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)




 