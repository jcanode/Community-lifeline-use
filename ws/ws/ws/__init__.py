"""
The flask application package.
"""

from flask import Flask
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from pymongo import MongoClient
import os

# Set up database connection
client = MongoClient("localhost:27017")
mongoDB=client["animal-rescue"]

# Set up app
app = Flask(__name__)

# Set up Monogo Engine
db = MongoEngine(app)

# Cross Site Request Forgery
csrf = CSRFProtect(app)

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# App config
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

import ws.views
