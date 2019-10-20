from flask_login import UserMixin
from ws import db
 
class User(UserMixin, db.Document):
    # User authentication information
    email = db.StringField()
    password = db.StringField()
