import joblib
import numpy as np

model = joblib.load("model/latest_model.pkl")

def predict(data):
    features = np.array([[data["feature1"], data["feature2"]]])
    return model.predict(features)[0]