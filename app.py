import json
from flask import Flask, request, Response
from flask_cors import CORS
from clean import clean_comment
from textblob import TextBlob

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

@app.route("/predict/", methods=["GET", "POST"])
def predict():
    comments = []
    rating = 0
    
    if request.method == "POST":
        comments = request.json["comments"]
    for comment in comments:
        temp = TextBlob(clean_comment(comment)).sentiment.polarity
        print(clean_comment(comment) + ": " + str(temp))
        rating += temp

    if rating >= 5:
        rating = 5.0
    else:
        if len(comments) > 0:
            rating = (rating/len(comments) + 1) * (5)/(2) * 1.2
    
     
    return Response(json.dumps({"rating" : rating}), mimetype='application/json')

