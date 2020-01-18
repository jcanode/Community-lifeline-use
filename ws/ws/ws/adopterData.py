from ws import mongoDB, app
from flask import render_template
"""
AnimalType = "dog" 
homeType = "appartment"
homeStatus = "own"
planToMove = ""
blackList = False
age = 5
"""

@app.route("/adopterData")
def adopterData(): 
    mongoDB.adopters.insert_one({

        "name": "justin",
        "pass": "void",
        "email": "jcanode@my.gcu.edu",
        "score": 0,
    })
    return render_template(
        'index.html',
        title='Adopter test')
    