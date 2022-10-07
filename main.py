from flask import Flask,render_template,url_for,request
import pandas as pd 
import numpy as np

import pickle

# load the model from disk
loaded_model=pickle.load(open('Models\RF_model.pkl', 'rb'))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def main():
    if request.method == 'POST':
        T, TM, Tm, H, VV, V, VM = float(request.form['T']), float(request.form['TM']), float(request.form['Tm']), float(request.form['H']), float(request.form['VV']), float(request.form['V']), float(request.form['VM'])
        
        df = pd.read_csv('Data/Final_Data/final_combine.csv')
        d_f = pd.DataFrame(data=[[ T, TM, Tm, H, VV, V, VM]])

        my_prediction = loaded_model.predict(d_f)
        # my_prediction=my_prediction.tolist()
        return render_template('index.html', predicted_pm = my_prediction)

if __name__ == "__main__":
    app.run(debug = True)
