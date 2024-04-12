from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route('/')
def get_data():
    # create db
    con = sqlite3.connect("temporary.db")
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS weather(day TEXT, temperature TEXT)')
    cur.execute(f'INSERT INTO waether VALUES ("TEST day", "92")')
    con.commit()

    # read the data we just wrote
    res = cur.execute('SELECT * FROM weather')
    return res.fetchall()


if __name__ == '__main__':
    app.run()
