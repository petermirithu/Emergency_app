from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))
class Source:
    '''
    Source class to define source objects
    '''
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('Password attribute cannot be read')

    # Generating password hash
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    # Verify password
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'


class Emergency(db.Model):
    __tablename__ = 'emergency'

    id = db.Column(db.Integer,primary_key =True)
    victim = db.Column(db.String,index = True)
    category = db.Column(db.String(255))
    description = db.Column(db.String(255))
    location = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default = datetime.utcnow)

    # save emergency
    def save_emergency(self):
        db.session.add(self)
        db.session.commit()

    # get all emergencies by category
    @classmethod
    def get_emergencies(cls,category):
        emergencies = Emergency.query.filter_by(category=category).all()
        return emergencies

    def __repr__(self):
        return f'Emergency {self.category}'    

class Conversation(db.Model):   
    '''
    class that contains conversation table
    '''
    __tablename__="conversation"

    id=db.Column(db.Integer,primary_key=True)
    emergency_id=db.Column(db.Integer())
    convo=db.Column(db.String(255))
    posted_by=db.Column(db.String(255))
    posted_on=db.Column(db.DateTime,default = datetime.utcnow)

    def save_convo(self):
        '''
        function that saves a new convo
        '''        
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_convos(clc,id):
        '''
        function that gets all convos for that particular emergency
        '''
        convos=Conversation.query.filter_by(emergency_id=id).all()
        return convos

class Reply(db.Model):   
    '''
    class that contains reply table
    '''
    __tablename__="reply"

    id=db.Column(db.Integer,primary_key=True)
    convo_id=db.Column(db.Integer())
    reply=db.Column(db.String(255))
    posted_by=db.Column(db.String(255))
    posted_on=db.Column(db.DateTime,default = datetime.utcnow)

    def save_reply(self):
        '''
        function that saves a new reply
        '''        
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_replies(clc,id):
        '''
        function that gets all replies for that particular convo
        '''
        replies=Reply.query.filter_by(convo_id=id).all()
        return replies

class Solution(db.Model):
    '''
    this is responsible for making solutions
    '''
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String)
    title = db.Column(db.String)
    posted_by = db.Column(db.String)
    category = db.Column(db.String)
    posted_on = db.Column(db.DateTime, default = datetime.utcnow)

    # save solution
    def save_solution(self):
        db.session.add(self)
        db.session.commit()
    
    
class Subscribers(db.Model):
    '''
    Class that contains the subscribers table
    '''
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique=True,index = True)

    def save_subscribers(self):
        '''
        Function to save all the subscribed emails
        '''
        db.session.add(self)
        db.session.commit()






