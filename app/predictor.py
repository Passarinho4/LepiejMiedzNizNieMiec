from tensorflow import keras
import joblib
import pandas as pd
import numpy as np


class Predictor:
    FEATURES = ['sum', 'sin', 'cos', '0', '1', '2', '3', '4', '5', '6']
    TARGET = ['result']

    def __init__(self, sequence_length_days=10):
        self.model = keras.models.load_model('model/model.kers')
        self.features_df = pd.read_csv('model/features.csv')
        self.features_df['date'] = pd.to_datetime(self.features_df['date'], format='%Y-%m-%d')
        self.features_df = self.features_df.set_index('date')
        self.features_scaler = joblib.load('model/features_scaler.gz')
        self.target_scaler = joblib.load('model/target_scaler.gz')
        self.sequence_length_days = sequence_length_days

    def predict(self, date, prediction_horizon_days=7):
        index = self.features_df.index.get_loc(pd.to_datetime(date))

        features_data = self.features_df[self.FEATURES + self.TARGET]
        features_data[self.FEATURES] = self.features_scaler.transform(features_data[self.FEATURES])
        features_data[self.TARGET] = self.target_scaler.transform(features_data[self.TARGET])

        y_pred = []

        def prepare_for_iteration(f):
            x_data = features_data.iloc[index - self.sequence_length_days + f:index + f]
            if f > 0:
                x_data[self.TARGET[0]] = np.append(x_data[self.TARGET[0]][:-f].to_numpy(), y_pred)
            return x_data

        for f in range(prediction_horizon_days):
            x_f = np.array([prepare_for_iteration(f)])
            y_f = self.model.predict(x_f)[0][0]
            y_pred.append(y_f)

        return self.target_scaler.inverse_transform([y_pred]).tolist()[0]
