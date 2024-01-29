from flask import Flask, render_template, request
import pickle
from tensorflow.keras.models import load_model

app = Flask(__name__)


model= pickle.load(open('savedmodel2.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    nitrogen=float(request.form['nitrogen'])
    phosphorus=float(request.form['phosphorus'])
    potassium=float(request.form['potassium'])
    temperature=float(request.form['temperature'])
    humidity=float(request.form['humidity'])
    ph=float(request.form['ph'])
    rainfall=float(request.form['rainfall'])
    result=model.predict([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])# Replace with your actual prediction result
    return render_template('index.html',**locals())
        # return render_template('result.html', result=result)

        # return render_template('result.html', result=result)


  

if __name__ == '__main__':
    app.run(debug=True)
