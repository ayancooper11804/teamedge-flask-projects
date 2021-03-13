import os
from flask import Flask, render_template, request, json, jsonify, current_app as app

app = Flask(__name__)

movies_path = os.path.join(app.static_folder, 'data', 'movies.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>About</h1><p>Some Other Content</p>'

#Get all movies.
@app.route('/api/v1/movies/all', methods=['GET'])
def api_movies_all():

    #using with allows for opening and closing of file
    with open(movies_path, 'r') as jsondata:
        movies = json.load(jsondata)

    #no need to return an html template
    return jsonify(movies)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')