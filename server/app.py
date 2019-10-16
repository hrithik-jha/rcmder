from flask import Flask, request, redirect, url_for, flash, jsonify
import json
import pandas as pd
import numpy as np
from Movie.mov import recommendations
from Music.rec import get_recommendations

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/movie', methods=["POST"])
def movie_id():
    if 'title' in request.args:
        title = request.args.get('title')
    else:
        return "Error: No Id field provided."
    
    #print(title)
    #rec = recommendations(id)
    l = []
    l = recommendations(title)
    #print(rec)

    return jsonify({'recommendations': l})


@app.route('/music', methods=["POST"])
def music_id():
    if 'name' in request.args and 'album in request.args':
        name = str(request.args.get('name'))
        album = str(request.args.get('album'))
    else:
        return "Error: No Id field provided."
    
    #print(title)
    #rec = recommendations(id)
    l = []
    l = get_recommendations(name, album)
    #print(rec)

    return jsonify({'recommendations': l})


app.run(debug=True)
