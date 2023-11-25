from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Resource
from sqlalchemy import and_, func


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
    category = request.args.get('category')
    keyword_str = request.args.get('q')

    keywords = keyword_str.split(' ') if keyword_str else []

    #if category and keywords:
    # if keywords != []:
    #     for i in keywords:
    #         results = Resource.query.filter(
    #             Resource.resource_type.ilike(f"%{category}%") &
    #             (Resource.resource_name.ilike(f"%{keywords}%") | Resource.resource_type.ilike(f"%{keyword}%"))
    #         ).all()
    # else:
    #     results = []
    if keywords != []:
        for i in keywords:
            results = Resource.query.filter(
                    Resource.resource_type.ilike(f"%{category}%") &
                    and_(*[Resource.keywords.ilike(f"%{i}%")])).limit(3).all()
    else:
        results = []

    return render_template('search.html', results=results, user=current_user)

# views.route('/filter', methods=['POST'])
# def filter():
#     """Collects user input and search the database for closest match.
#     The search works by Finding matches between values the user enters in "explicit 
#     fields" (e.g Category) and values found int the database. This method help 
#     in filtering by explicit values.
    
#     """
#     user_input = request.form["q"]
#     return user_input
