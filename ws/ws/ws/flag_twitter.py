import twitter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from bson.objectid import ObjectId
import string
from ws import mongoDB, app
from flask import Flask, render_template, redirect, url_for, request, jsonify

api = twitter.Api(consumer_key="ZhsPtnsPyqjDxhoY5M4cqdeGQ",
                  consumer_secret="DoRV7nMrh1YgdedBXDREauf5RgL99B2A9HylMY7c5Jze0gHBJ2",
                  access_token_key="1168917740754632704-MRxIFBnWcgU99udZyjpkbhYOBdQCd7",
                  access_token_secret="cWwMSisSCH5zosSsw9WHRSkcxaEwRpI6W73LtOptpwqd9")

@app.route("/flag_tweets")
def flag_tweets():
    id = request.args.get("id") 

    adopter = mongoDB.adopters.find_one({ "_id": ObjectId(id) })

    flaggedTweets = []
    count = 0

    if adopter != None and "twitter_username" in adopter:
        print(adopter)

        tweets = api.GetUserTimeline(screen_name=adopter["twitter_username"], count=50)

        stop_words = stopwords.words('english') + list(string.punctuation) + ["’", "‘"]

        ps = PorterStemmer()

        flags = mongoDB["social-media-flags"].find({ "social_media_twitter": True })
        flags = [ps.stem(flag["text"]) for flag in flags]
        for tweet in tweets:
            word_tokens = word_tokenize(tweet._json["text"])
    
            flaggedWords = []
            for w in word_tokens: 
                if w not in stop_words: 
                    w = ps.stem(w)
                    if w in flags:
                        flaggedWords.append(w)
  
            if len(flaggedWords) > 0:
                flaggedTweets.append({ "social_media": "twitter", "tweet": tweet._json, "flags": flaggedWords })
        count = len(flaggedTweets)
    return jsonify({ "recordsTotal": count, "recordsFiltered": count, "data": flaggedTweets })