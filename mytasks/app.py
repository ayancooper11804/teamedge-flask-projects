from flask import Flask, render_template
from sense_emu import SenseHat
from flask_apscheduler import APScheduler
import sqlite3

sense = SenseHat()

app = Flask(__name__)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()