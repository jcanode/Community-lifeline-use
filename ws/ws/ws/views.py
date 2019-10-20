"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ws import app, models, mongoDB, db, login_manager
from .forms import LoginForm, RegisterForm
from flask import request, redirect, render_template, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@login_manager.user_loader
def getUserById(id):
    user = mongoDB.users.find_one({"_id": id})
    json.loads(data, object_hook=lambda d: namedtuple('User', d.keys())(*d.values()))
    return User.get(id)

def getUserByEmail(email):
    return mongoDB.users.find_one({"email": email})

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        anyErr = False

        # Validate no user exists with email
        user = getUserByEmail(form.email.data)
        if user != None:
            flash("Email already exists in database.", category='error')

        # Enter user only if there are no errors
        if not anyErr:
            mongoDB.users.insert_one({
                "email": form.email.data,
                "password": generate_password_hash(form.password1.data),
                "status": 0
            })
            flash("User successfully registered!", category='success')
            return redirect(request.args.get("returnurl") or url_for("login"))
    return render_template('register.html', title='register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = getUserByEmail(form.email.data)
        # Verify user found and check password
        if user != None and check_password_hash(user["password"], form.password.data):
            login_user(user)
            flash("Logged in successfully", category='success')
            return redirect(request.args.get("returnurl") or url_for("home"))
        flash("Wrong email or password", category='error')
    return render_template('login.html', title='login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))