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
        "AnimalType": "hackaztest",
        "homeType":"hackaztest",
        "homeStatus":"hackaztest",  
        "planToMove": "",
        "do-not-adopt": False,
        "Previous Pets": "yes",
        "sprayed": False,
        "years owned": 5,
        "vetInfo": {
            'currentVet': 'yes',
            'emergencyVet':'yes'
        },
        "criminal record": False,        
        'lengthOfStay': 0,
        "score": 0,
    })
    return render_template(
        'index.html',
        title='Adopter test')
    