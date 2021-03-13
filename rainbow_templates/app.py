from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Ayan's Rainbow"

@app.route('/red')
def red():
    color = 'red'
    return render_template('red.html, color = color')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')