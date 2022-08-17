from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# source xicor_env/bin/activate  


# from distutils.log import debug

from flask_cors import CORS
from email import message

from chat import get_response

app = Flask(__name__)
CORS(app)



# @app.get("/")
# def index_get():
#     return render_template("web_main_2_javas.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #TODO: check if text is valid
    
    # count += 1
    
    response = get_response(text)
    message = {"answer":response}
    print(message)
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
    
