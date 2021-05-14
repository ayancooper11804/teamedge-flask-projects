from flask import Flask, render_template, current_app as app, redirect, url_for, request 
from sense_hat import SenseHat
from flask_apscheduler import APScheduler
import sqlite3

sense = SenseHat()

app = Flask(__name__)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/', methods=(['GET', 'POST']))
def index():
    if request.method == 'POST':
        task = request.form['task']
        date = request.form['date']
        return render_template('index.html', task = task, date = date)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')