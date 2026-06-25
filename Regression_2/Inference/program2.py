import numpy as np
from flask import Flask,render_template,request
import pickle
#create a Flask app
app = Flask(__name__)

#load the model
with open('./model.pkl','rb') as file:
    model = pickle.load(file)

#add routes root route
@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')
#add routes for prediction
@app.route('/predict', methods=['POST'])
def predict():
    sat_score = float(request.form(['sat_score']))
    gpa = model.predict([[sat_score]])
    return render_template('index.html', prediction=f"Predicted GPA: {gpa[0]:.2f}")

#run the app
app.run(host="0.0.0.0",port=5500,debug=True)