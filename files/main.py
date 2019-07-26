import os
from datetime import datetime
import pytz
from pytz import timezone
import flask
from flask import Flask, render_template, request, redirect, url_for, session
import requests
import json
app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def get_weather():
    if request.form:
        city_one = request.form['city_one']
        url_one = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=76213925c4e0771dbabb037e3a681e74".format(city_one)
        r_one = (requests.get(url_one)).json()
        weather_one = {
        'temp': r_one['main']['temp'],
        'description': r_one['weather'][0]['description'],
        'city': r_one['name'], 
        'country': r_one['sys']['country'],
        'humidity': r_one['main']['humidity']
        }
        

        city_two = request.form['city_two']
        url_two = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=76213925c4e0771dbabb037e3a681e74".format(city_two)
        r_two = (requests.get(url_two)).json()
        weather_two = {
        'temp': r_two['main']['temp'],
        'description': r_two['weather'][0]['description'],
        'city': r_two['name'],
        'country': r_two['sys']['country'],
        'humidity': r_two['main']['humidity'] 

        }
      
        return render_template("city.html", weather_one=weather_one, weather_two=weather_two)
     
    else:
        return render_template("base.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)