from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from datetime import datetime, timedelta
from flask import jsonify
import json


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class DataPoint:
    def __init__(self, date, value):
        self.date = date
        self.value = value
    
    def toJSON(self):
        return self.__dict__


@app.route("/dupa")
@cross_origin()
def hello():
    date_str = request.args.get('date')
    date_object = datetime.strptime(date_str, "%Y-%m-%d")
    delta = timedelta(days=1)
    arr = [DataPoint(date_object.strftime("%Y-%m-%d"), 12), 
    DataPoint((date_object + delta).strftime("%Y-%m-%d"), 2), 
    DataPoint((date_object + delta * 2).strftime("%Y-%m-%d"), 4), 
    DataPoint((date_object + delta * 3).strftime("%Y-%m-%d"), 15),
    DataPoint((date_object + delta * 4).strftime("%Y-%m-%d"), 7),
    DataPoint((date_object + delta * 5).strftime("%Y-%m-%d"), 18),
    DataPoint((date_object + delta * 6).strftime("%Y-%m-%d"), 38),
    DataPoint((date_object + delta * 7).strftime("%Y-%m-%d"), 1)]
    data_points_json = [dp.toJSON() for dp in arr]
    return jsonify(data_points_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)

