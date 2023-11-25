# Module to provide backend support to parse through database
# and find 3-5 most related resources. 
import nltk
from nltk.corpus import wordnet
nltk.download('omw-1.4')
from website import views
from flask import Blueprint, render_template, request, redirect, url_for, Flask, jsonify
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy


# Keywords that will be removed from users description, if available, 
# to optimize search
low_priority_keywords = ['can', 'has', 'if', 've', "don't", 'weren', 'we', 'ain', 'above',
                          'at', 'each', 'll', "that'll", 'is', 'other', "weren't", 'isn',
                        'doing', "wouldn't", 'couldn', 'shouldn', "mustn't", 'i', 'this',
                        'both', 'by', 'own', 'aren', 'for', 'once', 'not', "aren't", 'having',
                        'am', 'its', "should've", 'now', 'out', 'in', "shan't", 'why', "should"
                        , 'some', 'haven', 'was', 'his', 'she', 'themselves', "wasn't", "you"
                        , 'into', 'how', 'didn', 'few', 'her', "you'll", 'from', 'very', "does",
                        'before', 'only', 'should', 'our', 'yourself', 'their', 'while', "couldn't",
                        'were', 'below', 'who', "you're", 'any', 'there', 'ourselves', 'my', 'because',
                        'to', 'don', 'nor', 'through', 'had', 'doesn', 'won', 'more', 'a', 'did', 'such',
                        'just', 'be', 'here', 're', 'that', 'but', 'and', 'so', "isn't", 'of', 'further',
                        'or', "needn't", 'me', 'does', 'too', 'd', 'been', 'an', "you'd", 'do',
                        'over', 'where', 'mustn', 'yours', 'until', "she's", 'same', 'are', 'being',
                        "hadn't", 'them', 'after', 'have', 's', "didn't", "won't", 'yourselves', 'him',
                        'myself', 'than', 'it', 'whom', 'they', 'then', 'ma', 'herself', 'again', 
                        'himself', 'with', 'o', 'what', 'off', 'all', 'needn', "hasn't", 'most', 'up',
                        'your', 'the', 'against', 'no', 'you', 'these', 'when', 'as', 'between', 'under',
                        'will', 'about', 'on', 'during', 'm', 't', 'hers', 'theirs', 'would', 'ours',
                        'itself', 'those', 'hadn', 'hasn', "haven't", 'which', "it's", "mightn't", 'down', 
                        'he', 'i']


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
db = SQLAlchemy(app)

views.views.route('/filter', methods=['POST'])
def filter():
    """Collects user input and search the database for closest match.
    The search works by Finding matches between values the user enters in "explicit 
    fields" (e.g Category) and values found int the database. This method help 
    in filtering by explicit values.
    
    """
    #with app.app_context():
    user_input = request.form.get('q')
    return jsonify({'user_input': user_input})

def refine_keywords():
    """Finds "high yield" words in a user description, persist those words into
      a list, and use each of those words to help calculate similarity score. 

    Returns:
        list: the list of high yeild keywords
    """
    return "refined_list"

def calculate_similarity(filter_results, keywords):
    """Calculate the scoring of each resource model based on synonym
    match with keywords from the user's description. Similarity is 
    calculated based on number of synonyms shared by a resource db model 
    and the each keyword. 

    Args:
        filter_results (list): preliminary list of resource models that match
        explicit fields.
        keywords (list): keywords whose synonyms will be used to compare
        agaisnt each filter_result model in the database.

    Returns:
        dict: a dict with keys the similairy score and value the resource
    """
    return "simialirity scorings"

def complete_search(resource_similarity):
    """Get the the top 3, if applicable, most similar resources and return
       them to a search results html template.

    Args:
        resource_similarity (dict): the dictionary to get the 3 most similar
        scored resources from.

    Returns:
        html: rendered html template with list of resources
    """
    return "render_template(search_results.html, results=results)"


# if __name__ == "__main__":
#     complete_search(calculate_similarity(filter(), refine_keywords()))

    #UNIT TESTS - SEARCH FEATURE 
    # Testing filter() 
        #Initialize a list of ResourceModels 
        


