from flask import Blueprint, render_template, request, redirect, url_for, make_response
from flask_login import login_required, current_user
from .models import Resource
from search import *

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

    category = request.args.get('category')
    keyword_str = request.args.get('q')

    keywords = keyword_str.split(' ') if keyword_str else []
    keywords = remove_low_priority_keywords(keywords)
    results = []

    if keywords:
        results = Resource.query.filter(
            Resource.resource_type.ilike(f"%{category}%")).limit(5)
        keywords1 = keywords[:-1]
    else:
        keywords1 = keywords

    filtered_results = set()
    filtered_results = find_resource_by_keyword_similarity(results, keywords1)

    response = make_response(render_template(
        'search.html', results=list(filtered_results), user=current_user))
    response.headers['Cache-Control'] = 'store'

    return response
