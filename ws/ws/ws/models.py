from flask_login import UserMixin
from ws import db
 
class User(UserMixin, db.Document):
    # User authentication information
    email = db.StringField()
    password = db.StringField()
    status = db.StringField()

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False