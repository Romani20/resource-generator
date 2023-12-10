import pandas as pd
from website import db, models
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv, search, json 

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
                keywords_json = search.convert_description_to_array(row[2])
                
                feedback_string = row[5]
                feedback_list = [float(value) for value in feedback_string.split()]
                feedback_json = json.dumps(feedback_list)

                resource = models.Resource(id = hash(row[0]), resource_name=row[0], resource_type=row[1],
                                    link_to_website=row[3], keywords=keywords_json, email=row[4], feedback=feedback_json)
                    
                db.session.add(resource)
                db.session.commit()
                db.session.close()

def calculate_ratings(rating, resource_name):
    """_summary_

    Args:
        rating (_type_): _description_

    Returns:
        _type_: _description_
    """

    return 0

manually_write_resources_to_database()
