from .models import *
import unit_tests
from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
import logging

#authenticate = Flask(__name__)

authenticate = Blueprint('authenticate', __name__)

@authenticate.route("/")
def index():
    return render_template("home.html")

@authenticate.route('/login', methods=['GET', 'POST'])
def login():
    """Log a user into a the webpage's homepage. It accecpts
        user's email and password: if the email does not exist or
        crednetials are incorrect, then user is a flashed an error message
        and are prompted to either sign up or re-enter details.
    """
    #if request.method == 'POST':
    # email = "dummy_entered_email"
    # password = "dummy_entered_password"

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
            new_user = User(id=hash(first_name), email=email, first_name=first_name, password=password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html", user=current_user)

authenticate.route("/search")
def search():
    q = request.args.get("q")
    #print(q)
    if q:
        logging.info("Not empty")

    if q:
        results = Resource.query.filter(Resource.resource_name.icontains(q)).limit(2).all()
    else:
        results = []

    return render_template("search.html", results=results)


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