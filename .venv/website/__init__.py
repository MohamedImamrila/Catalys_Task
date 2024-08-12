from flask import Flask
from datetime import timedelta
from .auth import auth
from .views import views

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'catalys'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
    

    app.register_blueprint(auth)
    app.register_blueprint(views)

    return app