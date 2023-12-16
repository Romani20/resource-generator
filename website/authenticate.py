from .models import *
from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from . import db
import json

authenticate = Blueprint('authenticate', __name__)

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
                session.permanent = False
                session.modified = True
                login_user(user, remember=False)
                return render_template("home.html", user=current_user)
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
            return redirect(url_for('authenticate.login'))

    return render_template("sign_up.html", user=current_user)