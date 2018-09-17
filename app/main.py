#from flask import Flask

#app = Flask(__name__)

#@app.route("/")

import recommender as rec

def hello():
    return "Hey I'm using Docker! And... I found " + getClusters() + " clusters..."

if __name__ == "__main__":
    #app.run(host="0.0.0.0", debug=True, port=80)
    recom = rec.Recommender()

