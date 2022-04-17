from datetime import datetime
from todoapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Ticket(db.Model, UserMixin):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,  nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,  nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime,  nullable=True)
    name = db.Column(db.String(250), nullable=False) 
    label = db.Column(db.String(250), nullable=False, default='light') 
    status = db.Column(db.String(250), nullable=False, default='todo') 

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,  nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,  nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime,  nullable=True)
    username = db.Column(db.String(20), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # author = db.relationship('Comment', backref='written_by')

class Comment(db.Model, UserMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,  nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,  nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime,  nullable=True)
    content = db.Column(db.Text, nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey(Ticket.id), nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    ticket = db.relationship(Ticket, foreign_keys=ticket_id)
    user = db.relationship(User, foreign_keys=user_id)
    
    
      
  