from flask import Flask
from flask_cors import CORS
import datetime
from flask import request
from aqi import get_past_aqi_data, get_predicted_aqi, get_next_hour, parse_aqi_data
from database_operations import get_data, store_data
from monitoring import add_processing_time, get_average_processing_time
import time

app = Flask(__name__)
CORS(app)


# gets the AQI number for the last week at the same hour that the user is querying
@app.route('/aqi')
def get_aqi():
    start = time.time()

    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    data = get_past_aqi_data(latitude, longitude)
    parsed_data = parse_aqi_data(data)
    now = datetime.datetime.now()
    next_hour = get_next_hour(now)
    predicted_aqi = get_predicted_aqi(parsed_data, next_hour)
    store_data(predicted_aqi, next_hour, now, latitude, longitude)

    processing_time = time.time() - start
    add_processing_time(processing_time)

    return predicted_aqi


@app.route('/get-past-predictions')
def get_past_predictions():
    start = time.time()

    data = get_data()

    processing_time = time.time() - start
    add_processing_time(processing_time)

    return data


@app.route('/metrics')
def get_metrics():
    return {"avg_processing_time": get_average_processing_time()}


@app.route('/health')
def get_health():
    return "200"


if __name__ == '__main__':
    app.run()
