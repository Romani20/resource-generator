from sqlalchemy.sql import func
from . import db
from flask_login import UserMixin

#db = SQLAlchemy() /

class Resource(db.Model):
    """Model forming the schema of information stored in our database
       for each resource. 

    Args:
        db (SQL database): the datbase in which information from the 
        model is persited. 
    """

    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(100), nullable=False)
    link_to_website = db.Column(db.String(255), nullable=False)
    resource_type = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    keywords = db.Column(db.String(500), nullable=False)

class User(db.Model, UserMixin):
    """Model forming the schema to represent each user of our service

    Args:
        db (SQL datbase): the database for which information for users
        is persisted.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    