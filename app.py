from flask import Flask, request
from flask_cors import CORS
# from model import form_review

app = Flask(__name__)
CORS(app)

@app.route("/predict/", methods=["GET", "POST"])
def predict():
    comments = {}
    
    if request.method == "POST":
        comments = request.json["comments"]
    print(comments)
    return {"prediction": comments}

