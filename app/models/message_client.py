from app import db

class Message_Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'),nullable = False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'),nullable = False)
    def __repr__(self):
        return '<User {}>'.format(self.email)