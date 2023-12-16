from flask import Flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .authenticate import authenticate

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(authenticate, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'authenticate.signup'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @app.route('/add_resource_page')
    def add_resource_page():
        return render_template('Add_resource_page.html', user=User)

    @app.route('/rate_resource_page')
    def rate_resource_page():
        return render_template('rate_resource_page.html', user=User)
    
    @app.route('/toc_page')
    def terms_of_conditions_page():
        return render_template('terms.html', user=User)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
