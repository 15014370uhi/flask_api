from flask import Flask, request
from flask_cors import CORS
import json
import os
from myLogisticRegression import getPredictions 

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Welcome to safe streets machine learning flask server"

@app.route("/predict", methods=["POST"])
def runPredictionModel():
    data = request.get_json(silent=True)
    month = data.get("month")
    year = data.get("year")
    lat = data.get("lat")
    lon = data.get("lon")
    sector = data.get("sector")

    # call machine learning function with data
    result = getPredictions(month, year, lat, lon, sector)   
    results_JSON = json.dumps(result)
   
   # print("results_JSON: ", results_JSON)
    
    return results_JSON

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))   
   #app.run(port=5000)
