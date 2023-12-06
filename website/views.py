from flask import Blueprint, render_template, request, redirect, url_for, make_response
from flask_login import login_required, current_user
from .models import Resource
from sqlalchemy import and_
import spacy
from search import find_resource_by_keyword_similarity


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """_summary_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        category = request.form.get("category")
        q = request.form.get("q")

        if q and category:
            return redirect(url_for('views.search_results', category=category, q=q))

    return render_template('home.html', user=current_user)


@views.route('/search_results', methods=['GET'])
def search_results():
    """_summary_

    Returns:
        _type_: _description_
    """
    #nlp = spacy.load("en_core_web_md")
    category = request.args.get('category')
    keyword_str = request.args.get('q')

    keyword = keyword_str.split(' ') if keyword_str else []
    keywords1 = []
    size = len(keyword)
    if keyword[size-1] == "":
        keywords1 = keyword[:-1]
    else:
        keywords1 = keyword

    # if len(keyword_str) > 0:
    if keywords1 != []:
        results = (Resource.query.filter(Resource.resource_type.ilike(f"%{category}%")).limit(5))
    else:
        results = []

    result = find_resource_by_keyword_similarity(results, keyword_str)

    response = make_response(render_template(
        'search.html', results=list(result), user=current_user))
    response.headers['Cache-Control'] = 'no-store'

    return response