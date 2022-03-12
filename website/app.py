from flask import Flask, render_template, request, url_for
import requests
import numpy as np
#import pickle
#from datetime import date, timedelta

# website used: https://codepen.io/atunnecliffe/pen/gpKzQw
# nlp app: https://towardsdatascience.com/develop-a-nlp-model-in-python-deploy-it-with-flask-step-by-step-744f3bdd7776


app = Flask(__name__)

#def load_model():
#  return pickle.load(open(‘iris_model.pkl’, ‘rb’))

@app.route("/")
def input_text():
  #response = requests.get(NBA_url).json()
  #input = []
  #return render_template("index.html", output = make_prediction(input))
  return render_template("index_css_new.html")

@app.route("/predict", methods=['POST'])
def make_prediction():
  #input = request.form.values()
  #output = input
  #if request.method == 'POST':
  message = request.form.get("input_text")
    #message =  request.POST.values()
    #result = [message]
  return render_template("result.html", output = message) 
    
  #features = [float(x)  for x in request.form.values()] 
    
  #values = [np.array(features)] 
    #model = load_model() 
    #prediction = model.predict(input) 
    #result = labels[prediction[0]] 
    #return render_template(‘index_new.html’, output = result) 
