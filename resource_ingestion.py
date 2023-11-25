import pandas as pd
from website import db, models
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv

# Resources and their metadata are ingested from two sources:
# primary - manually created json objects holding resource information
# secondary - user added data 
# This module will ingest from json files into database.

# Sample json objects:
# [
#     {"id": 1, 
#      "resource_name": "Writing Workshop"
#      "resource_type": "Academics"
#      "keywords": {"write", "essay", "English", "improve writing"}},

#    {"id": 2, 
#      "resource_name": "Resource Center"
#      "resource_type": "Equity"
#      "keywords": {"social", "diversity", "pantry", "fgli"}}
# ]

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
                resource = models.Resource(id = hash(row[0]), resource_name=row[0], resource_type=row[1],
                                        link_to_website=row[3], keywords=row[2], email=row[4])
        # for _, row in df.iterrows():
        #     # resource = models.Resource(id=hash(row['resource_name']),
        #     #                        resource_name=row["resource_name"],
        #     #                        link_to_website=row.get("link_to_website", "").strip(),
        #     #                        resource_type=row.get("resource_type", "").strip(),
        #     #                        email=row.get("email", "").strip(),
        #     #                        keywords=row.get("keywords", "").strip())

        #     resource = models.Resource(
        #     resource_name=row["resource_name"].strip(),
        #     link_to_website=row["link_to_website"].strip(),
        #     resource_type=row["resource_type"].strip(),
        #     email=row["email"].strip(),
        #     keywords=row["keywords"].strip())

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