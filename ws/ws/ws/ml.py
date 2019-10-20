
from flask import Flask, request, jsonify
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from pymongo import MongoClient
import os
from ws import mongoDB, app
from ws.views import col_result, col_result2
from bson.objectid import ObjectId

@app.route('/score_single')
def score_single():
    id = request.args.get("id")

    data = mongoDB.adopters.find_one({ "_id": ObjectId(id) })
    score = perform_score(data)
    return jsonify(score)

@app.route('/score_multi')
def score_multi():
    data = mongoDB.adopters.find()
    result = []
    for item in data: 
        score = perform_score(item)
        if score != None:
            result.append(score)
    return jsonify(result)

def perform_score(inData):
    AnimalType = col_result(inData,"AnimalType")

    homeStatus= col_result(inData,"homeStatus")
    homeType= col_result(inData,"homeType")
    previousSprayed = col_result(inData,"sprayed")
    age = col_result(inData,"years owned")
    planToMove= col_result(inData,"planToMove")
    currentVet = col_result2(inData,"vetInfo", "currentVet")
    emergencyVet = col_result2(inData,"vetInfo", "currentVet")
    doNotAdopt = col_result(inData,"do-not-adopt")
    criminalRecord = col_result(inData,"criminal record")
    lengthOfStay = col_result(inData,"lengthOfStay")

    if age == '':
        return None

    score = 50 

    w1 = 2
    w2 =  5
    w3 = 10
    w4 = 10
    w5 = 10
    w6 = 8

    if AnimalType == "dog":
        if homeType == "appartment":
            score = score - w1
    if homeStatus == "own":
        score = score + w2
    else:
        score = score - w2
    if (previousSprayed): 
        score = score + w4
    else:
        score = score - w4/2
    if age > 4:
        score = score + (age - 4)
    else: 
        score = score - (4-age)
    if (currentVet):
        score = score + w4
    if (emergencyVet):
        score = score + w5
    if (planToMove):
        score = score - w6
    score = score + lengthOfStay
    if ("do-not-adopt"==True):
        msg = "do not adopt list"
        score = 0
    if ("criminal record"==True):
        msg = "there is a criminal record"
        score = 0
    #output Score
    print (score)
    if (score > 80):
        msg = "This is a very good canadate for adoption"
    elif(50 <= score <= 80):  
        msg = "this may be a good canatate for adoption"
    elif(25 <= score < 50):
        msg = "this is not a good canadate for adoption"
    elif(score < 25):
        msg = "this is a very bad canadate for adoption"
    mongoDB.adopters.update({ "_id": ObjectId(inData["_id"]) }, { "$set":  { "score": score }})
    return (score,msg)
