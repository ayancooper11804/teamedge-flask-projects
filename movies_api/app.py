import os
from flask import Flask, render_template, request, json, jsonify, current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>About</h1><p>Some Other Content</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')