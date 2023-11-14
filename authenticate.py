#Module to provides backend support for user authentication
# using the Flask micro framework.

def login():
    """Log a user into a the webpage's homepage. It accecpts
        user's email and password: if the email does not exist or
        crednetials are incorrect, then user is a flashed an error message
        and are prompted to either sign up or re-enter details.
    """

    return "logged in"

def logout():
    """Logs out user from the main homepage to the login in page. 
    """

    return "logged out"

def signup():
    """Accepts an email, name, password, and confirmation password
    from the user and create an account for them to access our service.
    If the email already exists, user is prompted to enter a new email -or
    login. The required fields will have a number of requirements, but at 
    minimum, the password should be at least 5 characters long and their
    name should be atleast 1 character long.
    """

    return "signed_up"