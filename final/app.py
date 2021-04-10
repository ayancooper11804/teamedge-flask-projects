from flask import Flask, render_template, current_app as app, redirect, url_for, request
from sense_emu import SenseHat
import sqlite3

sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Get and Post requests
@app.route('/success' ,methods = ['POST'])
def success():
    name = request.form['name']
    messages = request.form['message']
    sense.show_message(name  + " " + messages)
    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO messages (name, nessage) VALUES((?),(?))",(name, messages))
    conn.commit()
    conn.close()
    return render_template('success.html' ,name = name ,message = messages)

@app.route('/all')
def all():
    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.curso()
    messages = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        message = {'name': row[0], 'message': row[1]}
        messages.append(message)
    conn.close()
    return render_template('all.html', message = messages)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')