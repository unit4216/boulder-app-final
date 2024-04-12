from flask import Flask
import sqlite3
from flask_cors import CORS
import requests
import datetime
from flask import request
from aqi import get_past_aqi_data, get_predicted_aqi, get_next_hour, parse_aqi_data
from database import get_data, store_data

app = Flask(__name__)
CORS(app)


# gets the AQI number for the last week at the same hour that the user is querying
@app.route('/aqi')
def get_aqi():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    data = get_past_aqi_data(latitude, longitude)
    parsed_data = parse_aqi_data(data)
    now = datetime.datetime.now()
    next_hour = get_next_hour(now)
    predicted_aqi = get_predicted_aqi(parsed_data, next_hour)
    store_data(predicted_aqi, next_hour, now, latitude, longitude)
    return predicted_aqi


@app.route('/get-past-predictions')
def get_past_predictions():
    return get_data()


if __name__ == '__main__':
    app.run()
