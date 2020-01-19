"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, jsonify
# from flask_restful import Resource, Api
from ws import app, models, mongoDB, db, login_manager, auth
from .forms import LoginForm, RegisterForm, CSVUploadForm
# from flask_wtf.csrf import CSRFProtect    
from flask import request, redirect, render_template, url_for, flash, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import csv
import json
from io import StringIO
from datetime import timedelta
import pandas as pd

# csrf = CSRFProtect(app)

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


@app.route('/api/register', methods=['GET', 'POST']) #TODO REDO THIS TO ACCEPT JSON POST
def register():
    if request.method=='POST':
        # data = request.get_data()
        # print (data)
        user = request.get_json()

        # temp = json.loads(data)
        
        # data = temp[0]
        # print (data)

        # user = auth.getUserByEmail(data)
        # user=data.email
        # print (user)
        if user != None:
            flash("Email already exists in database.", category='error')
            anyErr = True
            if not anyErr:
                mongoDB.users.insert_one(user)
            # flash("User successfully registered", category=success)
            # return 'ok'
        return 'ok'
    # return render_template('')
 #form = RegisterForm()
  #  if request.method == 'POST' and form.validate_on_submit():
   #     anyErr = False
#
 #       # Validate no user exists with email
  #      user = auth.getUserByEmail(form.email.data)
    #    if user != None:
     #       flash("Email already exists in database.", category='error')
      #      anyErr = True
#
        # Enter user only if there are no errors
 #       if not anyErr:
  #          mongoDB.users.insert_one({
   #             "name": form.name.data,
    #            "email": form.email.data,
     #           "password": generate_password_hash(form.password1.data),
      #          "isAdmin": False,
       #         "status": 0
        #    })
         #   flash("User successfully registered!", category='success')
          #  return redirect(request.args.get("returnurl") or url_for("login"))
#    return render_template('register.html', title='register', form=form)
		    
"""New JSON registration"""
 #   data = request.get_json()

  #  user = auth.getUserByEmail(data.email)
  #  if user != None:
  #      flash("Email already exists in database.", category='error')
  #      anyErr = True
 #   if not anyErr:
  #      mongoDB.user.insert_one(data)
   #     flash("User successfully registered", category=success)
  #      return redirect(request.args.get("returnurl") or url_for("login"))
   # return render_template('')

"""old registration form"""

@app.route('/', methods=['GET', 'POST'])
# Route for handling the login page logic

@app.route('/api/authentication', methods=['GET', 'POST']) #TODO REDO THIS TO ACCEPT JSON POST
def login():
    if method=='POST':
        user = request.get_json()
        form = LoginForm()
        if user != None and check_password_hash(user["password"], user.password):
            login_user(user, remember=True, duration=timedelta(days=90))
            flash("Logged in successfully", category='success')
            return redirect(request.args.get("returnurl") or url_for("home"))
            flash("Wrong email or password", category='error')
    return render_template('login.html', title='login', form=form)


@app.route('/login', methods=['GET', 'POST']) #
def token():
    user = request.get_json()
    form = LoginForm()
    if user != None and check_password_hash(user["password"], user.password):
        login_user(user, remember=True, duration=timedelta(days=90))
        flash("Logged in successfully", category='success')
        return redirect(request.args.get("returnurl") or url_for("home"))
        flash("Wrong email or password", category='error')
    return render_template('login.html', title='login', form=form)

"""old login form"""    
#form = LoginForm()
#    if request.method == 'POST' and form.validate_on_submit():
 #       user = auth.getUserByEmail(form.email.data)
  #      #Verify user found and check password
   #     if user != None and check_password_hash(user["password"], form.password.data):
    #        login_user(user, remember=True, duration=timedelta(days=90))
     #       flash("Logged in successfully", category='success')
      #      return redirect(request.args.get("returnurl") or url_for("home"))
       # flash("Wrong email or password", category='error')
#    return render_template('login.html', title='login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/api/users/<int:UID>')
def get_users(UID):
    output = []
    documents = mongoDB.users.find(  {"uid": UID} )
    for document in documents:
        output.append({
            "UID": col_result(document, "uid"),
            "name": col_result(document, "name"),
            "email": col_result(document, "email"),
            "status": col_result(document, "status"),
       })
    data = json.dumps(output[0])
    return data



@app.route('/api/users')
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



@app.route('/api/helpRequests/<int:UID>', methods=["GET", "POST"])
def getUsers(UID):
    if request.method=="POST":
        data = request.get_json()   
        data.append({"uid": UID})
        print(data)
        mongoDB.adopters.insert_one(data)
        flash("Request successfully submitted!", category='success')
        return 'ok'
    if request.method=="GET":
        output = []
        documents = mongoDB.adopters.find({"uid": UID})
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
            "data": output[0]
        })

# requestscount = 1
@app.route('/api/helpRequests', methods=["GET", "POST"])
def addRequest():
    if request.method=="POST":
        data = request.get_json()
        # UID = requestscount
        # requestscount += 1   
        # data.append({"uid": UID})
        print(data)
        mongoDB.adopters.insert_one(data)
        flash("Request successfully submitted!", category='success')
    return 'ok'
def col_result(document, key):
    if key in document:
        return document[key]
    return ""

def col_result2(document, key1, key2):
    if key1 in document and key2 in document[key1]:
        return document[key1][key2]
    return ""


# @app.route('/api/helpRequest/<int:uid>', methods=['POST'])
# @csrf.exempt
# def requestHelp(uid):
#         data = request.get_json()   
#         print(data)
#         mongoDB.adopters.insert_one(data)
#         flash("Request successfully submitted!", category='success')
#         return 'ok'



@app.route('/api/request/<int:uuid>', methods=["GET", "POST"])
def reslove_request(uuid):
    """Sent to"""
    helprequest = mongoDB.adopters.find_one({"uid": uuid})
    
    print(helprequest)
    return helprequest

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
    
