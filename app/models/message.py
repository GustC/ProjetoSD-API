from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False)
    message_client = db.relationship('Message_Client', backref='message', lazy='dynamic')
    def __repr__(self):
        return '<User {}>'.format(self.email)