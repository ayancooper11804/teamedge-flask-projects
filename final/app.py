from flask import Flask, render_template, current_app as app, redirect, url_for, request
from sense_hat import SenseHat

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
    return render_template('success.html' ,name = name ,message = messages)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')