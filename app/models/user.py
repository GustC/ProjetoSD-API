from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    company =  db.relationship('Company', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.email)

