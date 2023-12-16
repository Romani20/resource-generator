from unit_tests import genericUnitTest
import spacy
import json
from website import models

nlp = spacy.load("en_core_web_md")

# Keywords that will be removed from users description, if available,
# to optimize search. Words are generated from nlk module
low_priority_keywords = ['can', 'has', 'if', 've', "don't", 'weren', 'we', 'ain', 'above',
                         'at', 'each', 'll', "that", 'is', 'other', "weren't", 'isn',
                         'doing', "wouldn't", 'couldn', 'shouldn', "mustn't", 'i', 'this',
                         'both', 'by', 'own', 'aren', 'for', 'once', 'not', "aren't", 'having',
                         'am', 'its', "should've", 'now', 'out', 'in', "shan't", 'why', "should", 'some', 'haven', 'was', 'his', 'she', 'themselves', "wasn't", "you", 'into', 'how', 'didn', 'few', 'her', "you'll", 'from', 'very', "does",
                         'before', 'only', 'should', 'our', 'yourself', 'their', 'while', "couldn't",
                         'were', 'below', 'who', "you're", 'any', 'there', 'ourselves', 'my', 'because',
                         'to', 'don', 'nor', 'through', 'had', 'doesn', 'won', 'more', 'a', 'did', 'such',
                         'just', 'be', 'here', 're', 'that', 'but', 'and', 'so', "isn't", 'of', 'further',
                         'or', "need", 'me', 'does', 'too', 'd', 'been', 'an', "you'd", 'do',
                         'over', 'where', 'mustn', 'yours', 'until', "she's", 'same', 'are', 'being',
                         "hadn't", 'them', 'after', 'have', 's', "didn't", "won't", 'yourselves', 'him',
                         'myself', 'than', 'it', 'whom', 'they', 'then', 'ma', 'herself', 'again',
                         'himself', 'with', 'o', 'what', 'off', 'all', 'needn', "hasn't", 'most', 'up',
                         'your', 'the', 'against', 'no', 'you', 'these', 'when', 'as', 'between', 'under',
                         'will', 'about', 'on', 'during', 'm', 't', 'hers', 'theirs', 'would', 'ours',
                         'itself', 'those', 'hadn', 'hasn', "haven't", 'which', "it's", "mightn't", 'down',
                         'he', 'i', 'student', 'help', 'want', 'we', 'support', 'provide']


def remove_low_priority_keywords(user_description):
    """
    Removes words that aren't helpful for the searching process 
    from user's description by using the low priority keywords list above. 

    Args:
        user_description (str list): the usersn explicit request

    Returns:
        str list: a modified list with low priority words removed
    """
    new_list = []
    for i in user_description:
        if i.isalpha() and i.lower() not in (item.lower() for item in low_priority_keywords):
            new_list.append(i)

    return new_list


def convert_description_to_array(description):
    """
    Takes user's description and converts it into an a json dump
    , the format of keyords in databse.

    Args:
        description (str): a description of a user entered resource.

    Returns:
        json dump: non-low priority words dumped as array
    """
    refined_desc = []
    keywords_list = description.split(" ")

    refined_desc = remove_low_priority_keywords(keywords_list)

    return json.dumps(refined_desc)


def find_resource_by_keyword_similarity(results, keywords1):
    """Calculate the scoring of each resource model based on synonym
    match with keywords from the user's description. Similarity is 
    calculated based on number of synonyms shared by a resource db model 
    and the each keyword. 

    Args:
        filter_results (list): preliminary list of resource models that has
        explict category match.
        keywords (list): keywords whose synonyms will be used to compare
        agaisnt each filter_result model in the database.

    Returns:
        dict: a dict with keys the similairy score and value the resource
    """
    filtered_results = set()
    if results:
        for i in keywords1:
            for result in results:
                try:
                    resource_keywords = json.loads(result.keywords)
                    for processed_keyword in [nlp.vocab[keyword] for keyword in resource_keywords]:
                        for i in remove_low_priority_keywords(keywords1):
                            similarity_score = processed_keyword.similarity(
                                nlp.vocab[i])
                            if similarity_score >= 0.3:
                                filtered_results.add(result)
                except json.decoder.JSONDecodeError as e:
                    print(f"Error decoding JSON for result {result.id}: {e}")

    return filtered_results


if __name__ == "__main__":
    # UNIT TESTS - SEARCH FEATURE
    #testing remove_low_priority_keywords()
    strlist = ['i', 'want', 'food']
    modified = ['food']
    genericUnitTest(remove_low_priority_keywords, (strlist,), (modified,))

    print("\n")
    strlist = ['i', 'want', 'had']
    modified = []
    genericUnitTest(remove_low_priority_keywords, (strlist,), (modified,))


    # testing convert_description_to_array()
    print("\n")
    res = '["food"]'
    genericUnitTest(convert_description_to_array, ('i want food',), (res,))

    print("\n")
    res = '[]'
    genericUnitTest(convert_description_to_array, ('i had want',), (res,))


    # testing find_resource_by_keyword_similarity()
    res1 = models.Resource(keywords='["money", "economics", "finance"]')
    filtered_list = [res1]
    result = set([res1])

    # happy case 1 - exact match
    print("\n")
    genericUnitTest(find_resource_by_keyword_similarity,
                    (filtered_list, "I want some money".split(" ")), (result,))

    # happy case 1 - similar words: money and capital (sim = ~0.39)
    print("\n")
    genericUnitTest(find_resource_by_keyword_similarity,
                    (filtered_list, "I love capital".split(" ")), (result,))

    # all low-priority word case
    print("\n")
    genericUnitTest(find_resource_by_keyword_similarity, (filtered_list, "I want some".split(" ")), (set(),))

    # # non-low priority, low similarity word: money and lungs (sim = ~0.13)
    print("\n")
    genericUnitTest(find_resource_by_keyword_similarity, (filtered_list, "I want my lungs".split(" ")), (set(),))

    # part happy, part sad case
    print("\n")
    genericUnitTest(find_resource_by_keyword_similarity, (filtered_list,
                    "I want my money in my lungs".split(" ")), (result,))
