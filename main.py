from website import create_app
from resource_ingestion import *

app = create_app()

if __name__ == '__main__':
    #Checks the manual entries for newly added resources and 
    #write to database if it doesn't exists every time the app runs
    manually_write_resources_to_database()
    app.run(debug=True)
