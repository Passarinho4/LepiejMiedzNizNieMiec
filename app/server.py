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
    def __init__(self, date, value, error):
        self.date = date
        self.value = value
        self.error = error
    
    def toJSON(self):
        return self.__dict__


@app.route("/dupa")
@cross_origin()
def hello():
    date_str = request.args.get('date')
    date_object = datetime.strptime(date_str, "%Y-%m-%d")
    delta = timedelta(days=1)
    arr = [DataPoint(date_object.strftime("%Y-%m-%d"), 12, 1), 
    DataPoint((date_object + delta).strftime("%Y-%m-%d"), 2, 1), 
    DataPoint((date_object + delta * 2).strftime("%Y-%m-%d"), 4, 2), 
    DataPoint((date_object + delta * 3).strftime("%Y-%m-%d"), 15, 3),
    DataPoint((date_object + delta * 4).strftime("%Y-%m-%d"), 7, 3),
    DataPoint((date_object + delta * 5).strftime("%Y-%m-%d"), 18, 4),
    DataPoint((date_object + delta * 6).strftime("%Y-%m-%d"), 38, 4),
    DataPoint((date_object + delta * 7).strftime("%Y-%m-%d"), 10, 4)]
    data_points_json = [dp.toJSON() for dp in arr]
    return jsonify(data_points_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)

