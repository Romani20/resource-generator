import pandas as pd
from website import db, models
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv, json
from sqlalchemy import and_

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
                
                keywords_list=row[2].split(" ")
                keywords_json = json.dumps(keywords_list)

                # existing_resource = models.Resource.query.filter(
                #     models.Resource.resource_name.ilike(row[0]), 
                #     and_(models.Resource.resource_type.ilike(row[1])),
                #     and_(models.Resource.link_to_website.ilike(row[3]),
                #     and_(models.Resource.keywords.ilike(keywords_json))),
                #     and_(models.Resource.email.ilike(row[4])))
                
                # if existing_resource == []:
                resource = models.Resource(id = hash(row[0]), resource_name=row[0], resource_type=row[1],
                                    link_to_website=row[3], keywords=keywords_json, email=row[4])
                    
                db.session.add(resource)
                db.session.commit()
                db.session.close()


def write_user_inputted_resource_to_database():
    """Parses through the metadata the user enrers for a new resource to be added
       to the database and add the resource to the db. 

    Returns:
        None_: new resource is added to the database.
    """
    return "user_inputted"


manually_write_resources_to_database()