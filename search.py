# from PyDictionary import PyDictionary
# dictionary=PyDictionary()
import nltk
from nltk.corpus import wordnet
nltk.download('omw-1.4')
# from nltk.corpus import wordnet

# Module to provide backend support to parse through database
# and find 3-5 most related resources. 


# Keywords that will be removed from users description, if available, 
# to optimize search
low_priority_keywords = []

def search():
    """Collects user input and search the database for closest match.
    The search works by:
    1. Finding matches between values the user enters in "explicit 
    fields" and values found int the database. 
    2. It uses a data parsing approach where it finds "high yield" words 
    in a user description, persist those words into a list and find synonyms 
    for each of those words - which evetually are used to search the database.
    
    In worst case, if no close match is found, we'll return a category-
    appropriate match.
    """

    return "get_resource"

# synonyms = []

# for syn in wordnet.synsets("queer"):
#     for lm in syn.lemmas():
#              synonyms.append(lm.name())

# for i in synonyms:
#        if i == "gay":
#             print(True)
# print (set(synonyms))

