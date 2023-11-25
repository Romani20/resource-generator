from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Resource

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
    keyword = request.args.get('q')

    if category and keyword:
        results = Resource.query.filter(
            Resource.resource_type.ilike(f"%{category}%") &
            (Resource.resource_name.ilike(f"%{keyword}%") | Resource.resource_type.ilike(f"%{keyword}%"))
        ).all()
    else:
        results = []

    return render_template('search.html', results=results, user=current_user)
