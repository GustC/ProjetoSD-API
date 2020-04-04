from app import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(128))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'),nullable = False)
    message_client = db.relationship('Message_Client', backref='client', lazy='dynamic')

    def __repr__(self):
        return '<Client id = {} name = {} >'.format(self.id,self.name)

    def toMap(self):
        return {
            "id" : self.id, 
            "email" : self.email, 
            "name" : self.name,  
        }