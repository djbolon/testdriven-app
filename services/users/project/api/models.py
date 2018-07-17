# services/users/project/api/models.py


from project import db
import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'active': self.active
        }

class Exrate(db.Model):
    __tablename__ = "rates"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rate_from = db.Column(db.String(128), nullable=False)
    rate_to = db.Column(db.String(128), nullable=False)
    rate = db.Column(db.String(128), nullable=False)
    rate_date = db.Column(db.DateTime, nullable=False, default=datetime.date.today())
    
    def __init__(self, rate_from, rate_to, rate, rate_date):
        self.rate_from = rate_from
        self.rate_to = rate_to
        self.rate = rate
        self.rate_date = rate_date

    def rate_json(self):
    	return {
            'id': self.id,
            'rate_from': self.rate_from,
            'rate_to': self.rate_to,
            'rate': self.rate,
            'rate_date': self.rate_date
        }

class ListExrate(db.Model):
    __tablename__ = "listrates"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rate_from = db.Column(db.String(128), nullable=False)
    rate_to = db.Column(db.String(128), nullable=False)
    rate_date = db.Column(db.DateTime, nullable=False, default=datetime.date.today())
    
    def __init__(self, rate_from, rate_to):
        self.rate_from = rate_from
        self.rate_to = rate_to
        
        

    def rate_json(self):
    	return {
            'id': self.id,
            'rate_from': self.rate_from,
            'rate_to': self.rate_to,
            
        }
