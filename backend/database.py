import sqlite3
import datetime


def store_data(predicted_aqi: str, prediction_hour: int, now: datetime, latitude: str, longitude: str):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS predictions(aqi TEXT, prediction_hour TEXT, generated_at TEXT, latitude TEXT, longitude TEXT)')
    cur.execute(f'INSERT INTO predictions VALUES ("{predicted_aqi}", "{prediction_hour}", "{now}", "{latitude}", "{longitude}")')
    con.commit()


def get_data():
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute('PRAGMA table_info(predictions)')
    column_names = [column[1] for column in cur.fetchall()]

    res = cur.execute('SELECT * FROM predictions')
    rows = res.fetchall()

    parsed_data = [
        {
            column_names[0]: row[0],
            column_names[1]: row[1],
            column_names[2]: row[2],
            column_names[3]: row[3],
            column_names[4]: row[4],
        } for row in rows
    ]

    return parsed_data
