from src.config.app import db


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User('{self.name}')"
