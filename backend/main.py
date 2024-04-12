from flask import Flask
import sqlite3
from flask_cors import CORS
import requests
import datetime
from flask import request
from aqi import get_past_aqi_data, get_predicted_aqi, get_next_hour, parse_aqi_data

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
    return get_predicted_aqi(parsed_data, next_hour)


@app.route('/')
def get_data():
    # create db
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS weather(day TEXT, temperature TEXT)')
    cur.execute(f'INSERT INTO weather VALUES ("TEST day", "92")')
    con.commit()

    # read the data we just wrote
    res = cur.execute('SELECT * FROM weather')
    return res.fetchall()


if __name__ == '__main__':
    app.run()
