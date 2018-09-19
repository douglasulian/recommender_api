from flask import Flask, g
from recommender import *
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hey I'm using Docker!"


@app.route("/clusters")
def clusters():
    return json.dump(numpy.ndarray.tolist(getRecommender().clusters))

def getRecommender():
    if 'recommender' not in g:
        g.recommender = Recommender()
    return g.recommender

if __name__ == "__main__":
    recommender = getRecommender()
    app.run(host="0.0.0.0", debug=True, port=80)

