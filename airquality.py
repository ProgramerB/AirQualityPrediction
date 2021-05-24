import json
from time import time
from random import random
from flask import Flask, render_template, make_response, jsonify
import serial
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import random

air_q=":("
app = Flask(__name__)

def getSensorValue():
    ser=serial.Serial('COM6',9600)
    temp = float(ser.readline())
    global air_q
    if temp <= 50:
        air_q = 'Good'
    if temp > 50:
        air_q = 'Moderate'
    if temp > 100:
        air_q = 'Unhealthy for sensitive groups'
    if temp > 150:
        air_q = 'Unhealthy'
    if temp > 200:
        air_q = 'Very Unhealthy'
    if temp > 300:
        air_q = 'Hazardous'
    return temp


#ML
file = open("dataset/city_day.csv",'r')
dataframe1=pd.read_csv(file)
dataframe=dataframe1.dropna()
#print(dataframe)

def predict_aqi(component,aqi):
    features_aqi=["AQI"]
    X_aqi=dataframe[features_aqi]
    y_aqi=dataframe[component]

    X_train, X_test, y_train, y_test = train_test_split(X_aqi,y_aqi,random_state=0)
    #print(y_train)

    linreg=LinearRegression().fit(X_train,y_train)
    temp=linreg.predict([[aqi]])
    return float(temp[0])

#ML-END

def getAirQualityBucket():
    aqi=getSensorValue()
    #aqi=5
    if aqi < 50:
        return 'Good'
    if aqi < 100:
        return 'Moderate'
    if aqi < 150:
        return 'Unhealthy for sensitive groups'
    if aqi < 200:
        return 'Unhealthy'
    if aqi < 300:
        return 'Very Unhealthy'
    else:
        return 'Hazardous'
    
@app.route('/_aqibucket', methods= ['GET'])
def aqibucket():
    return jsonify(bucket = air_q)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/pm25_temp')
def pm25_temp():
    return render_template("pm25_web.html")

@app.route('/pm10_temp')
def pm10_temp():
    return render_template("pm10_web.html")

@app.route('/no_temp')
def no_temp():
    return render_template("no_web.html" )

@app.route('/no2_temp')
def no2_temp():
    return render_template("no2_web.html" )

@app.route('/nox_temp')
def nox_temp():
    return render_template("nox_web.html" )

@app.route('/nh3_temp')
def nh3_temp():
    return render_template("nh3_web.html" )

@app.route('/co_temp')
def co_temp():
    return render_template("co_web.html" )

@app.route('/so2_temp')
def so2_temp():
    return render_template("so2_web.html" )

@app.route('/o3_temp')
def o3_temp():
    return render_template("o3_web.html" )

@app.route('/live-data')
def live_data():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000, getSensorValue()]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/pm25')
def pm25():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000,predict_aqi("PM2.5",getSensorValue())]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/pm10')
def pm10():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000,predict_aqi("PM10",getSensorValue())]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/no')
def no():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000,predict_aqi("NO",getSensorValue())]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/no2')
def no2():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000,predict_aqi("NO2",getSensorValue())]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/nox')
def nox():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000,predict_aqi("NOx",getSensorValue())]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/nh3')
def nh3():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000,predict_aqi("NH3",getSensorValue())]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/co')
def co():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000,predict_aqi("CO",getSensorValue())]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/so2')
def so2():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000,predict_aqi("SO2",getSensorValue())]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/o3')
def o3():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000,predict_aqi("O3",getSensorValue())]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
