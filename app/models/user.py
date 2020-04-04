from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)    
    messages = db.relationship('Message', backref='user', lazy='dynamic')    

    def __repr__(self):
        return '<User {}, company_id {}>'.format(self.email,self.company_id)

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        import jwt
        import datetime
        from app import config
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                config.Config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    import jwt
    from app import config
    try:
        payload = jwt.decode(auth_token, config.Config.SECRET_KEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

