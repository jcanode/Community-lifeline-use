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

@app.route("/HelpRequest")
def adopterData(): 
    mongoDB.adopters.insert_one({

        "latitude": 33.509949,
        "longitude":  -112.127377,
        "name": "justin",
        "email": "jcanode@my.gcu.edu",
        "problem": 1,
        "description": "test"
    })
    return render_template(
        'index.html',
        title='Adopter test')
    