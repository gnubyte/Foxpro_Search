# @Author: Patrick Hastings
# @Date: 8-27-2017
# @Title: ORM wrapper
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    workPhone = db.Column(db.String(30))
    email = db.Column(db.String(120), index=True, unique=True)
    ptusername = db.Column(db.String(20))
    personalcell = db.Column(db.String(23))
    FirstName = db.Column(db.String(25))
    LastName = db.Column(db.String(25))
    jobtitle = db.Column(db.String(25))
    TextAllowed = db.Column(db.Integer)
    CallAllowed = db.Column(db.Integer)
    personalEmail = db.Column(db.String(120))
    username = db.Column(db.String(30))
    password = db.Column(db.String(100))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3    
    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)