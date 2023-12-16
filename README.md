# Project Description 
This project is an application that is going to suggest Wesleyan resources based on a keyword/words a user enters. It'll have a database to store all the available Wesleyan resources, requests from people, and the effectiveness of each resource in solving students' problems. Not only it is used for generating more information on resources, but also to keep track of resources that are highly in demand, resources students are in need of but aren't yet provided by Wesleyan, and even resources that aren't fully serving the purpose they are dedicated to. Additionally, users can also update the database for resources by adding resources themselves. 

# List of Proposed Features 
1. A sign in page 
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
- Run the file called nlp_treshhold.py to get the spacy training model
- Download DB Browser for SQLite app compatible with your device using this link: https://sqlitebrowser.org/dl/

# To run the project 

- Run the file main.py to run the website
- In the terminal, you will get a link that looks like "Running on http://127.0.0.1:5000", then go to that site.
  
  ## To access and view the database
      1. Open the 'DB Browser for SQLite' app
      2. Go to 'Open Database', find your repository folder, find the folder called 'instance', and then open 'database.db'
  
# Future directions or suggestions for additional features

- Using a cloud-based database that updates in real-time to ensure seamless synchronization of data
- Refining our search results by sorting the returned resource table in descending order based on ratings, meaning the highest-rated items should appear at the top.
- Implementing a mechanism to control the addition of inappropriate resources

# Notes and troubleshooting 
    1. You may have to open your database before running main.py - but either way should work.
    2. The first time you click on the link to access the website, it will take you to the signup page. This is the desired behavior.
        However, if you should click on the click again (in your terminal), it will take you to the main page. We have made several
        attempts to have the program not remember that you are logged in, but proper execution of that seems to require more learning.
        If you want to sign up for a new account, you can always go to the signup page from the home page. 
    3. Because the database is local, sometimes it might get closed after a while, and you might get an error that looks like this if you 
        try to add resource, feedback, search: "SQL error: database is locked". Try closing and opening the databse to refresh it.

