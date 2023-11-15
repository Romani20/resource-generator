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
#      "keywords": {"equity", "diversity", "pantry", "fgli"}}
# ]

def write_resources_to_database(resources):
    """Parses the json file and write each of its field to a MySQL database. 

    Args:
        resources (.json): the name of the json file whose objects are being 
                    parsed and written to table. 

    Returns:
        None: objects are added to table. 
    """
    return "resources added"
