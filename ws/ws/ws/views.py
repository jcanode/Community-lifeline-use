"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request
from ws import app, models, mongoDB, db, login_manager, auth
from .forms import LoginForm, RegisterForm
from flask import request, redirect, render_template, url_for, flash, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import csv
from io import StringIO
from datetime import timedelta

@app.route('/home')
@login_required
def home():
    #Renders the home page.
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/csv_view')
@login_required
def csv_view():
    #Renders the csv page.
    return render_template(
        'csv.html',
        title='CSV',
        year=datetime.now().year,
        message='Your csv page.'
    )

@app.route('/candidates')
@login_required
def candidates():
    #Renders the candidates page.
    return render_template(
        'candidates.html',
        title='Candidates',
        year=datetime.now().year,
        message='Import list of candidates here'
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        anyErr = False

        # Validate no user exists with email
        user = auth.getUserByEmail(form.email.data)
        if user != None:
            flash("Email already exists in database.", category='error')
            anyErr = True

        # Enter user only if there are no errors
        if not anyErr:
            mongoDB.users.insert_one({
                "email": form.email.data,
                "password": generate_password_hash(form.password1.data),
                "isAdmin:": False,
                "status": 0
            })
            flash("User successfully registered!", category='success')
            return redirect(request.args.get("returnurl") or url_for("login"))
    return render_template('register.html', title='register', form=form)

@app.route('/', methods=['Get', 'POST'])
# Route for handling the login page logic
@app.route('/login', methods=['Get', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = auth.getUserByEmail(form.email.data)
        #Verify user found and check password
        if user != None and check_password_hash(user["password"], form.password.data):
            login_user(user, remember=True, duration=timedelta(days=90))
            flash("Logged in successfully", category='success')
            return redirect(request.args.get("returnurl") or url_for("home"))
        flash("Wrong email or password", category='error')
    return render_template('login.html', title='login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/site_setting')
@login_required
def site_setting():
    #Renders the site settings page.
    return render_template(
        'site_setting.html',
        title='Site Settings',
        year=datetime.now().year,
        message='Your site settings page'
    )

@app.route('/user_list')
@login_required
def user_list():
    #Renders the user list page.
    return render_template(
        'user_list.html',
        title='User List',
        year=datetime.now().year,
        message='Your user list page.'
    )

@app.route('/jwt_controls')
def jwt_controls():
    #Renders the jwt controls page.
    return render_template(
        'jwt_controls.html',
        title='JWT Controls',
        year=datetime.now().year,
        message='Your jwt controls page'
    )

def csv_prepare_row(obj_data, col_names):
   result = []
   for key in obj_data:
       value = obj_data[key]
       if key not in col_names:
           col_names.append(key)
       result.insert(col_names.index(key), value)
   return result
@app.route('/csv_download')
def csv_download():
   table = request.args.get('table')
   if table != None:
       col_names = []
       si = StringIO()
       writer = csv.writer(si)
       # Get data
       documents = mongoDB[table].find()
       # Loop through rows
       for document in documents:
           writer.writerow(csv_prepare_row(document, col_names))
       # Return output
       output = make_response(",".join(col_names) + "\n" + si.getvalue())
       output.headers["Content-Disposition"] = "attachment; filename=export.csv"
       output.headers["Content-type"] = "text/csv"
       return output
   return redirect(url_for('csv_view'))

@app.route('/adopter_list')
def adopter_list():
   output = []
   documents = mongoDB.adopters.find()
   for document in documents:
       output.append({
           "name": document["name"]
       })
   count = len(output)
   return jsonify({
       "draw": 1,
       "recordsTotal": count,
       "recordsFiltered": count,
       "data": output
   })