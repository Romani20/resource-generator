from .models import *
from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for, Flask
from . import db, create_app
from search import convert_description_to_array as convert
from flask_sqlalchemy import SQLAlchemy
import json

authenticate = Blueprint('authenticate', __name__)

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

@authenticate.route("/")
def index():
    return render_template("home2.html")


@authenticate.route('/login', methods=['GET', 'POST'])
def login():
    """Log a user into a the webpage's homepage. It accecpts
        user's email and password: if the email does not exist or
        crednetials are incorrect, then user is a flashed an error message
        and are prompted to either sign up or re-enter details.
    """

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@authenticate.route('/logout')
@login_required
def logout():
    """Logs out user from the main homepage to the login in page. 
    """
    logout_user()
    return redirect(url_for('authenticate.login'))


@authenticate.route('/sign-up', methods=['GET', 'POST'])
def signup():
    """Accepts an email, name, password, and confirmation password
    from the user and create an account for them to access our service.
    If the email already exists, user is prompted to enter a new email -or
    login. The required fields will have a number of requirements, but at 
    minimum, the password should be at least 5 characters long and their
    name should be atleast 1 character long.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(id=hash(first_name), email=email,
                            first_name=first_name, password=password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


@authenticate.route('/')
def index_add_resource():
    # resources = Resource.query.all()
    return render_template('Add_resource_page.html', user=current_user)
    #  resources=resources)


@authenticate.route('/add_resource', methods=['POST'])
def add_resource():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db = SQLAlchemy(app)

    with app.app_context():
        resource_name = request.form['resource_name']
        link_to_website = request.form['link_to_website']
        resource_type = request.form['resource_type']
        email = request.form['email']
        keywords = request.form['keywords']

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

    return redirect(url_for('authenticate.index_add_resource'))


# Melat Added this

@authenticate.route('/')
def rate_resource_index():

    return render_template('rate_resource_page.html')


@authenticate.route('/submit_rating', methods=['POST'])
def submit_rating():
    """_summary_

    Returns:
        _type_: _description_
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

            db.session.commit()
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON for result: {e}")

    return redirect(url_for('views.home'))


# if __name__ == "__main__":
#     # login()
#     # logout()
#     # signup()

#     # #TESTING THE AUTHENTICATION FEATURE
#     # 1. testing login()

#     # login_happy_case
#     user = User(email="dummy@gmail.com", password="dummypassword")
#     email = "dummy@gmail.com"
#     password = "dummypassword"

#     unit_tests.genericUnitTest(login, (email, password, user), ("Correct_password",))

#     print("\n")
#     # login_in_incorrect_password
#     wrong_password = "wrong_dummypassword"
#     unit_tests.genericUnitTest(login, (email, wrong_password, user), ("Incorrect_password",))

#     # login_in_email_doesnt_exist - this test requirs application context to search the database

#     # 2. testing signup()

#     # signup_happy_case()
#     name = "Romani"
#     email = "dummy@gmail.com"
#     password = "dummypassword"
#     confirm = "dummypassword"

#     print("\n")
#     user = User(email=email, password=password)
#     unit_tests.genericUnitTest(signup, (email, name, password, confirm), (user.email,))

#     # signup_invalidname_case)
#     name = ""
#     print("\n")
#     unit_tests.genericUnitTest(signup, (email, name, password, confirm), ("Invalid name",))

#     # signup_short_password_case
#     name = "Romani"
#     password = "lol"
#     print("\n")
#     unit_tests.genericUnitTest(signup, (email, name, password, confirm), ("Password too short",))

#     # signup_passwords_don't_match
#     password = "dummypassword"
#     confirm = "dummypassword1"
#     print("\n")
#     unit_tests.genericUnitTest(signup, (email, name, password, confirm), ("Passwords don't match",))