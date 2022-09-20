from flask import Flask,render_template,url_for,request
import pandas as pd 
import numpy as np

import pickle

# load the model from disk
loaded_model=pickle.load(open('Models/XGboost_Model.pkl', 'rb'))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def main():
    if request.method == 'POST':
        T, TM, Tm, SLP, H, VV, V, VM = float(request.form['T']), float(request.form['TM']), float(request.form['Tm']), float(request.form['H']), float(request.form['VV']), float(request.form['V']), float(request.form['VM'])
        loaded_model_pm = loaded_model.predict([[T, TM, Tm, H, VV, V, VM]])

        # print(loaded_model_pm)

    return render_template("index.html", loaded_model_pm = np.round(loaded_model_pm,3))

if __name__ == "__main__":
    app.run(debug = True)
