import pandas as pd
from website import db, models
# import models
# from __init__ import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv, json
from sqlalchemy import and_
import search as search

# Resources and their metadata are ingested from two sources:
# primary - manually created json objects holding resource information
# secondary - user added data 
# This module will ingest from a csv into database.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
db = SQLAlchemy(app)

def manually_write_resources_to_database():
    """Parses the json file and write each of its field to a MySQL database. 

    Args:
        resources (.json): the name of the json file whose objects are being 
                    parsed and written to table. 

    Returns:
        None: objects are added to table. 
    """
    with app.app_context():
        db.session.query(models.Resource).delete()
        df = pd.read_csv("resource.csv", encoding="latin1")

        with open("resource.csv", 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                keywords_json = convert_description_to_array(row[2])
                resource = models.Resource(id = hash(row[0]), resource_name=row[0], resource_type=row[1],
                                    link_to_website=row[3], keywords=keywords_json, email=row[4])
                    
                db.session.add(resource)
                db.session.commit()
                db.session.close()

def convert_description_to_array(description):
    """_summary_

    Args:
        description (_type_): _description_

    Returns:
        _type_: _description_
    """
    refined_desc = []
    keywords_list = description.split(" ")

    for i in keywords_list:
        if i.lower() not in (item.lower() for item in search.low_priority_keywords):
            refined_desc.append(i)

    return json.dumps(refined_desc)

def write_user_inputted_resource_to_database():
    """Parses through the metadata the user enrers for a new resource to be added
       to the database and add the resource to the db. 

    Returns:
        None_: new resource is added to the database.
    """
    return "user_inputted"


manually_write_resources_to_database()