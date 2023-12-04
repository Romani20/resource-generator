from flask import Blueprint, render_template, request, redirect, url_for, make_response
from flask_login import login_required, current_user
from .models import Resource
from sqlalchemy import and_
import spacy
from . import db


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        category = request.form.get("category")
        q = request.form.get("q")

        if q and category:
            return redirect(url_for('views.search_results', category=category, q=q))

    return render_template('home.html', user=current_user)


@views.route('/search_results', methods=['GET'])
def search_results():
    nlp = spacy.load("en_core_web_md")
    category = request.args.get('category')
    keyword_str = request.args.get('q')

    keyword = keyword_str.split(' ') if keyword_str else []
    keywords1 = []
    size = len(keyword)
    if keyword[size-1] == "":
        keywords1 = keyword[:-1]
    else:
        keywords1 = keyword

    if keywords1 != []:
        results = (Resource.query.filter(
            Resource.resource_type.ilike(f"%{category}%")).limit(3))
    else:
        results = []

    if results != []:
        filtered_results = set()
        for result in results:
            keywords = result.keywords
            for processed_keyword in [nlp.vocab[keyword] for keyword in keywords]:
                for i in keywords1:
                    similarity_score = processed_keyword.similarity(
                        nlp.vocab[i])
                    if similarity_score >= 0.3:
                        filtered_results.add(result)

    response = make_response(render_template(
        'search.html', results=list(filtered_results), user=current_user))
    response.headers['Cache-Control'] = 'no-store'

    return response
