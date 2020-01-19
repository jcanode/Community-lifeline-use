"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, jsonify
# from flask_restful import Resource, Api
from ws import app, models, mongoDB, db, login_manager, auth
from .forms import LoginForm, RegisterForm, CSVUploadForm
from flask_wtf.csrf import CSRFProtect
from flask import request, redirect, render_template, url_for, flash, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import csv
import json
from io import StringIO
from datetime import timedelta
import pandas as pd

csrf = CSRFProtect(app)

# csrf_protect = CsrfProtect(app)
# api = restful.Api(app, decorators=[csrf.exempt])

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
    form=CSVUploadForm()
    return render_template(
        'csv.html',
        title='CSV',
        year=datetime.now().year,
        message='Your csv page.',
        form=form
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

@app.route('/users')
@login_required
def users():
    #Renders the users page.
    return render_template(
        'users.html',
        title='Users',
        year=datetime.now().year
    )

@app.route('/register', methods=['GET', 'POST']) #TODO REDO THIS TO ACCEPT JSON POST
def register():
    """New JSON registration"""
    # data = request.get_json()

    # user = auth.getUserByEmail(data.email)
    # if user != None:
    #     flash("Email already exists in database.", category='error')
    #     anyErr = True
    # if not anyErr:
    #     mongoDB.user.insert_one(data)
    #     flash("User successfully registered", category=success)
    #     return redirect(request.args.get("returnurl") or url_for("login"))
    # return render_template('')

"""old registration form"""
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
                "name": form.name.data,
                "email": form.email.data,
                "password": generate_password_hash(form.password1.data),
                "isAdmin": False,
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
   output = []
   documents = mongoDB.users.find()
   for document in documents:
       output.append({
           "name": col_result(document, "name"),
           "email": col_result(document, "email"),
           "status": col_result(document, "status"),
           "isAdmin": col_result(document, "isAdmin")
       })
   count = len(output)
   return jsonify({
       "draw": 1,
       "recordsTotal": count,
       "recordsFiltered": count,
       "data": output
       })

@app.route('/jwt_controls')
@login_required
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
@login_required
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

@app.route('/api/users')
@login_required
def getUsers():
   output = []
   documents = mongoDB.adopters.find()
   
   for document in documents:
       output.append({
           "name": col_result(document, "name"),
           "email": col_result(document, "email"),
           "problem": col_result(document, "problem"),
           "latitude": col_result(document, "latitude"),
           "longitude": col_result(document, "longitude"),
            "description": col_result(document, "description"),
            "uid": col_result(document, "uid"),
            "id": str(document["_id"])
       })
   count = len(output)
   return jsonify({
       "draw": 1,
       "recordsTotal": count,
       "recordsFiltered": count,
       "data": output
   })

def col_result(document, key):
    if key in document:
        return document[key]
    return ""

def col_result2(document, key1, key2):
    if key1 in document and key2 in document[key1]:
        return document[key1][key2]
    return ""

@app.route('/csv_upload', methods=["POST"]) 
@login_required
def csv_upload():
   form = CSVUploadForm()
   if form.validate_on_submit():
       headers = form.headers.data
       if len(headers) > 0:
           headers = headers.split(',')
       data = pd.read_csv( form.file.data )
       if len(headers) <= 0:
           headers = data.columns.values
       for i in range(0, data["_id"].count()):
           row={}
           for field in headers:
               row[field]=str(data.iloc[i][field])
           mongoDB[form.table.data].insert(row)
       flash("Successfully uploaded CSV", category='success')
   return render_template(
       'csv.html',
       title='CSV',
       year=datetime.now().year,
       message='Your csv page.',
       form=form
   )



@app.route('/api/requestHelp/<int:uid>', methods=['POST'])
@csrf.exempt
# @csrf.exempt
def requestHelp(uid):
        data = request.get_json()
        # temp = json.dumps(data)
        # content = json.loads(temp)
        # content = JSON.parse(content).
        print(data)
        # Enter user only if there are no errors
        # if not anyErr:
        mongoDB.adopters.insert_one(data)
            # "name": content[name],
            # "email": content.email,
            # # "password": generate_password_hash(form.password1.data),
            # # "isAdmin": False
            # "problem": content.problem,
            # "description": content.description,
            # "latitude": content.latitude,
            # "longitude": content.longitude,
        
        flash("Request successfully submitted!", category='success')
        return 'ok'

@app.route('/social_media_flags')
@login_required
def social_media_flags():
    id = request.args.get("id") 
    return render_template(
       'social_media_flags.html',
       title='Social Media Flags',
       year=datetime.now().year,
       userID = id
   )

@app.route('/api/resolve/<int:uuid>', methods=["GET", "POST"])
@login_required
def reslove_request(uuid):
    """Sent to"""
    helprequest = mongoDB.adopters.find_one({"uid": uuid})
    
    data = request.get_json()

    #after it has been resolved
        #mongoDB.adopters.delete_one({"uid": uuid})
    """

    
    resolve
    {
        "victim": "string", 
        "help": "string",
        "victim": "string"
    }
    """
    