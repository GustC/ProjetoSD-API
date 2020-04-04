from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(14), index=True, unique=True)
    ramo = db.Column(db.String(128))
    user = db.relationship('User', backref='company', lazy='dynamic') 
    clients = db.relationship('Client', backref='company', lazy='dynamic')    
    def __repr__(self):
        return '<Company {}>'.format(self.cnpj)
