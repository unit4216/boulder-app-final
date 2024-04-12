from flask import Flask
import sqlite3
from flask_cors import CORS
import requests
import datetime

app = Flask(__name__)
CORS(app)


# gets the AQI number for the last week at the same hour that the user is querying
@app.route('/data')
def get_api_data():
    url = 'https://air-quality-api.open-meteo.com/v1/air-quality'
    params = {
        "latitude": 42.3662,
        "longitude": 71.0621,
        "hourly": ["us_aqi"],
        "past_days": 7,
        "forecast_days": 0
    }
    resp = requests.get(url, params=params)
    data = resp.json()

    parsed_data = []
    for index, hour in enumerate(data['hourly']['time']):
        aqi = data['hourly']['us_aqi'][index]
        parsed_data.append({"time": hour, "aqi": aqi})

    now = datetime.datetime.now()
    # this gets hour in 24h format (e.g. 16)
    # we want to get the next hour
    next_hour = now.hour + 1 if now.hour != 23 else 0
    # filter for current hour (date is in format ISO but missing seconds e.g. `YYYY-MM-DDTHH:MM`
    filtered_data = [x for x in parsed_data if int(x["time"].split('T')[1].split(':')[0]) == next_hour]

    aqi_points = [x['aqi'] for x in filtered_data]

    total = 0
    for aqi in aqi_points:
        total = total + aqi
    average = total / len(aqi_points)

    return str(average)


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
