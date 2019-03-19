from flask import Flask, request, redirect, url_for, flash, jsonify
import json
import pandas as pd
import numpy as np
from Movie.mov import recommendations

app = Flask(__name__)
@app.route('/')
def hello():
    return "Sup"

@app.route('/movie', methods=["POST"])
def movie_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No Id field provided."
    
    #rec = recommendations(id)
    l = []
    l = recommendations(id)
    #print(rec)

    return jsonify({'recommendations': l})

'''
@app.route('/music', methods=["POST"])
def music_id():
'''    

app.run(debug=True)
