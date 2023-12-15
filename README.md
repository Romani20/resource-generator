# Project Description 
This project is an application that is going to suggest Wesleyan resources based on a keyword/words a user enters. It'll have a database to store all the available Wesleyan resources, requests from people, and the effectiveness of each resource in solving students' problems. Not only it is used for generating more information on resources, but also to keep track of resources that are highly in demand, resources students are in need of but aren't yet provided by Wesleyan, and even resources that aren't fully serving the purpose they are dedicated to. Additionally, users can also update the database for resources by adding resources themselves. 

# List of Proposed Features 
1. A login button to authenticate if a user is a Wesleyan member
2. A main page with the following features:
    - A search bar to enter keywords (for the user)
    - A pop-up of all the resources generated from the search   
    - A hamburger icon on the side with options to "Logout", view "Terms of Conditions", and "Add Resources"
      
 # Stakeholders & Users 

 Stakeholders
- Software Engineers - Romani, Melat, Professor Roberts 
- Wesleyan University
- Resources provided by all members of Wesleyan University

 Users
- Wesleyan University 
- Resource providers (only members of Wesleyan University)
- Resource users (to both members and non-members of Wesleyan University)
  
# Prerequisites and installation instruction

To launch this website successfully, you'll need to install a few essential modules. The following suggestions
assume that Python and Pip are already installed on your device.
- Pip install the following packages:
        - flask
        - flask_sqlalchemy
        - pandas
        - spacy
        - spacy_wordnet  
- Run the file called nlp_treshhold to get the spacy training model
- Downlaod DB Browser for SQLite app compatible to your device using this link: https://sqlitebrowser.org/dl/


# To run the project 

- Run the file main.py to run the website
- In the terminal, you will get a link that looks like "Running on http://127.0.0.1:5000", then go to that site.
  
  ## To access and view the database
      1. Open the DB Browser for SQLite app
      2. Go to 'Open Database', find your repository folder, find the folder called instance and then open database.db
  





