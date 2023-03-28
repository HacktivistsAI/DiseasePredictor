from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests

application = Flask(__name__) # initializing a flask app
app=application


@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/sign.html',methods=['GET'])  
def signinPage():
    return render_template("sign.html")

@app.route('/step-1.html',methods=['GET'])  
def step1Page():
    return render_template("step-1.html")

@app.route('/step-2.html',methods=['GET', 'POST'])  
def step2Page():
    return render_template("step-2.html")


@app.route('/step-3.html',methods=['GET'])  
def step3Page():
    return render_template("step-3.html")

@app.route('/step-4.html',methods=['GET'])  
def step4Page():
    return render_template("step-4.html")

@app.route('/step-5.html',methods=['GET'])  
def step5Page():
    return render_template("step-5.html")


@app.route('/step-6.html',methods=['GET'])  
def step6Page():
    return render_template("step-6.html")


if __name__ == "__main__":
    app.run(debug=True)