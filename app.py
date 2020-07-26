from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict/", methods=["GET", "POST"])
def predict():
    comments = {}
    
    if request.method == "POST":
        comments = request.json["comments"]
    
    return {"prediction": "2"}