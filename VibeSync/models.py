from .extensions import db
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    posts = relationship('Post', back_populates='author', lazy=True)

class Post(db.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=False)
    created = Column(db.DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship('User', back_populates='posts')