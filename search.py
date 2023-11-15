# Module to provide backend support to parse through database
# and find 3-5 most related resources. 
import resource_model
import nltk
from nltk.corpus import wordnet
nltk.download('omw-1.4')

# Keywords that will be removed from users description, if available, 
# to optimize search
low_priority_keywords = []

def filter():
    """Collects user input and search the database for closest match.
    The search works by Finding matches between values the user enters in "explicit 
    fields" (e.g Category) and values found int the database. This method help 
    in filtering by explicit values.
    
    """

    return "filtered_resources"

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


if __name__ == "__main__":
    complete_search(calculate_similarity(filter(), refine_keywords()))

    #UNIT TESTS - SEARCH FEATURE 
    # Testing filter() 
        #Initialize a list of ResourceModels 
        


