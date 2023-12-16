from flask import Blueprint, render_template, request, redirect, url_for, make_response, Flask, flash
from flask_login import login_required, current_user
from .models import Resource
from search import *
from . import db
from search import convert_description_to_array as convert
from flask_sqlalchemy import SQLAlchemy
import time

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """To directs the user to the main page, send user to the sign up
    page when the website opens, as well as rednder search results 
    when a search is made.

    Returns:
        html template: render of or redirection to approprate page based on context.
    """
   
    if request.method == 'POST':
        category = request.form.get("category")
        q = request.form.get("q")

        if q and category:
            return redirect(url_for('views.search_results', category=category, q=q))
    return render_template("home.html", user=current_user)


@login_required
@views.route('/search_results', methods=['GET'])
def search_results():
    """Supprt user search requests by sending a dictionary of 
    found resoures to user.

    Returns:
        html template: sends results to the search.html template.
    """

    category = request.args.get('category')
    keyword_str = request.args.get('q')

    keywords = keyword_str.split(' ') if keyword_str else []
    keywords = remove_low_priority_keywords(keywords)
    results = []

    if keywords:
        results = Resource.query.filter(Resource.resource_type.ilike(f"%{category}%")).limit(5)

    filtered_results = set()
    filtered_results = find_resource_by_keyword_similarity(results, keywords)

    final = {}
    for i in filtered_results:
        final[i] = json.loads(i.feedback)
        
    response = make_response(render_template('search.html', results=final, user=current_user, refresh=1))
    response.headers['Cache-Control'] = 'no-store'

    return response

@login_required
@views.route('/add_resource')
def index_add_resource():
    """Renders the add_resource page when they click
        'Add resource' or when their attempt to add resource fails.

    Returns:
        html template: the template shown
    """
    return render_template('Add_resource_page.html', user=current_user)


@login_required
@views.route('/add_resource', methods=['POST'])
def add_resource():
    """Process user's resource addition, by ingesting it to the website
    and making user';s know if the respource was added or not by flahing messages.

    Returns:
        html template: template remains after the user adds a resource
    """

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db = SQLAlchemy(app)

    with app.app_context():
        resource_name = request.form['resource_name']
        link_to_website = request.form['link_to_website']
        resource_type = request.form['resource_type']
        email = request.form['email']
        keywords = request.form['keywords']

        if db.session.query(models.Resource).filter(
                    models.Resource.resource_name.ilike(f"%{resource_name}%")).first() is not None:
            flash("Resource already exists.", category='error')
        else: 
            rating, count, roster = json.dumps([0.0, 0.0]), 0, json.dumps([])
            new_resource = Resource(
                resource_name=resource_name,
                link_to_website=link_to_website,
                resource_type=resource_type,
                email=email,
                keywords=convert(keywords),
                feedback=rating,
                feedback_count=count,
                rated_by_roster=roster
            )

            db.session.add(new_resource)
            db.session.commit()
            db.session.close()
            flash("Resource added!", category='success')

    return redirect(url_for('views.index_add_resource'))


@views.route('/submit_rating')
def rate_resource_index():
    """Rendering the rate resource page.

    Returns:
        html template: the rate resource page
    """
    return render_template('rate_resource_page.html', user=current_user)


@views.route('/submit_rating', methods=['POST'])
def submit_rating():
    """Processes user's feedback, ingesting them into the database.

    Returns:
        html tenplate, db write: writes the rating the databse, and 
        redirects the user home.
    """
    resource_name = request.form.get('resource_name')
    accessibility = float(request.form.get('accessibility'))
    effectiveness = float(request.form.get('effectiveness'))
    updated_acc = 0
    updated_eff = 0

    resource = Resource.query.filter(Resource.resource_name.ilike(f"%{resource_name}%")).first()

    if resource:
        try:
            user_email = current_user.email
            existing_raters = json.loads(resource.rated_by_roster)

            if user_email not in existing_raters:
                existing_raters.append(user_email)

                feed_count = resource.feedback_count + 1
                curr_rating = json.loads(resource.feedback)
                updated_rating = []
            
                updated_acc = (curr_rating[0] + accessibility)/(feed_count)
                updated_eff = (curr_rating[1] + effectiveness)/(feed_count)
                
                updated_rating.append(updated_acc)
                updated_rating.append(updated_eff)

                resource.feedback = json.dumps(updated_rating)
                resource.rated_by_roster = json.dumps(existing_raters)
                resource.feedback_count = feed_count
                flash("Thanks for your feedback!", category='success')
            else:
                flash("You already rated this resource.", category='error')
            db.session.commit()
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON for result: {e}")

    return redirect(url_for('views.rate_resource_index'))