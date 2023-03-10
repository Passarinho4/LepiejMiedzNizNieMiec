from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from datetime import datetime, timedelta
from flask import jsonify
from predictor import Predictor


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

predictor = Predictor()


class DataPoint:
    def __init__(self, date, value, error):
        self.date = date
        self.value = value
        self.error = error

    def toJSON(self):
        return self.__dict__


@app.route("/predict")
@cross_origin()
def predict():
    date_str = request.args.get('date')
    date_object = datetime.strptime(date_str, "%Y-%m-%d")

    predicted = predictor.predict(date_object)
    delta = timedelta(days=1)
    arr = [
        DataPoint((date_object + delta * (n + 1)).strftime("%Y-%m-%d"),
                  predicted[n],
                  predictor.error_for_horizon(n)
                  ) for n in range(7)]
    data_points_json = [dp.toJSON() for dp in arr]
    return jsonify(data_points_json)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)

