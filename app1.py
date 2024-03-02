from flask import Flask, render_template, request

import pickle

import pandas as pd

app = Flask(__name__)

model= pickle.load(open('model_rf_12.pkl','rb'))

@app.route('/')

def home():
    return render_template('health_insurance.html')

@app.route("/predict",methods=['POST'])

def predict():
    age = float(request.form['age'])
    sex = float(request.form['gender'])
    bmi = float(request.form['BMI'])
    children = float(request.form['noofchildren'])
    smoker = float(request.form['Are you Smoker'])
    result=str(model.predict([[age, sex, bmi, children,smoker]])[0])
    return result


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)