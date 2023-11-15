#Module to provides backend support for user authentication
# using the Flask micro framework.
from flask import Blueprint, render_template, request, flash, redirect, url_for
import models
import unit_tests

authenticate = Blueprint('auth', __name__)

#@authenticate.route('/login', methods=['GET', 'POST'])
def login(email, password, user):
    """Log a user into a the webpage's homepage. It accecpts
        user's email and password: if the email does not exist or
        crednetials are incorrect, then user is a flashed an error message
        and are prompted to either sign up or re-enter details.
    """
    #if request.method == 'POST':
    # email = "dummy_entered_email"
    # password = "dummy_entered_password"

    if user:
        if user.password == password:
            return "Correct_password"
        else:
            # Raise error
            return "Incorrect_password"
    else:
        # Raise email doesn't exist
        return "Email doesn't exist"

def logout():
    """Logs out user from the main homepage to the login in page. 
    """

    return "logged out"

def signup(email, name, password, confirm_password):
    """Accepts an email, name, password, and confirmation password
    from the user and create an account for them to access our service.
    If the email already exists, user is prompted to enter a new email -or
    login. The required fields will have a number of requirements, but at 
    minimum, the password should be at least 5 characters long and their
    name should be atleast 1 character long.
    """
    if len(name) < 1:
        # flash user error
        return "Invalid name"
    elif len(password) < 5:
        # flash user error
        return "Password too short"
    elif password != confirm_password:
        # flash user error
        return "Passwords don't match"
    else:
        # flash user success
        new_user = models.User(email=email, password=password)
    return new_user.email

if __name__ == "__main__":
    # login()
    # logout()
    # signup()

    # #TESTING THE AUTHENTICATION FEATURE 
    # 1. testing login()

    # login_happy_case
    user = models.User(email="dummy@gmail.com", password="dummypassword")
    email = "dummy@gmail.com"
    password = "dummypassword"

    unit_tests.genericUnitTest(login, (email, password, user), ("Correct_password",))

    print("\n")
    # login_in_incorrect_password
    wrong_password = "wrong_dummypassword"
    unit_tests.genericUnitTest(login, (email, wrong_password, user), ("Incorrect_password",))

    # login_in_email_doesnt_exist - this test requirs application context to search the database

    # 2. testing signup()

    # signup_happy_case()
    name = "Romani"
    email = "dummy@gmail.com"
    password = "dummypassword"
    confirm = "dummypassword"

    print("\n")
    user = models.User(email=email, password=password)
    unit_tests.genericUnitTest(signup, (email, name, password, confirm), (user.email,))

    # signup_invalidname_case)
    name = ""
    print("\n")
    unit_tests.genericUnitTest(signup, (email, name, password, confirm), ("Invalid name",))

    # signup_short_password_case
    name = "Romani"
    password = "lol"
    print("\n")
    unit_tests.genericUnitTest(signup, (email, name, password, confirm), ("Password too short",))

    # signup_passwords_don't_match
    password = "dummypassword"
    confirm = "dummypassword1"
    print("\n")
    unit_tests.genericUnitTest(signup, (email, name, password, confirm), ("Passwords don't match",))
