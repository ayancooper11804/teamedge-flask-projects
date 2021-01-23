from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>About</h1><p>Some Other Content</p>'

@app.route('/dynamic')
def dynamic():

    greeting="Welcome to 2021!"
    friends = ["Jordan", "Juno", "Jeremy", "Danield", "Darryl"]
    return render_template('dynamic.html', greeting=greeting, friends=friends)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
