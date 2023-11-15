from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class wes_resource(db.Model):
    """Model forming the schema of information stored in our database
       for each resource. 

    Args:
        db (SQL database): the datbase in which information from the 
        model is persited. 
    """

    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(100), nullable=False)
    link_to_website = db.Column(db.String(100), nullable=False)
    resource_type = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    keywords = db.Column(db.ARRAY, nullable=False)
    