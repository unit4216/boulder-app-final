import requests
import datetime


def get_next_hour(now: datetime):
    return now.hour + 1 if now.hour != 23 else 0


def get_past_aqi_data(latitude: str, longitude: str):
    url = 'https://air-quality-api.open-meteo.com/v1/air-quality'
    params = {
        "latitude": latitude,
        "longitude": longitude,
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

    return parsed_data


def get_predicted_aqi(parsed_data: list[dict], hour: int):

    # filter for current hour (date is in format ISO but missing seconds e.g. `YYYY-MM-DDTHH:MM`
    filtered_data = [x for x in parsed_data if int(x["time"].split('T')[1].split(':')[0]) == hour]

    aqi_points = [x['aqi'] for x in filtered_data]

    total = 0
    for aqi in aqi_points:
        total = total + aqi
    average = total / len(aqi_points)

    return str(average)
