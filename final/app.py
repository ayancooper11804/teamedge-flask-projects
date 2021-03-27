from flask import Flask, render_template, current_app as app, redirect, url_for, request
from sense_hat import SenseHat

sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Get and Post requests
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' & name

@app.route('/login' ,methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success' ,name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success' ,name = user)) 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')