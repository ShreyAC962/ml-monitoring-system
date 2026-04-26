import mlflow 
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
import joblib # To save/load trained models
import pandas as pd

df = pd.read_csv("data/sample_stream.json") # laod data from a JSON file into a DataFrame

X = df[["feature1", "feature2"]] # input features - independent variables
y = df["label"] # target variable - what we want to predict

model = RandomForestClassifier()

# Training the model using all the data
model.fit(X, y)

# Evaluate model accuracy on same data (training accuracy)
accuracy = model.score(X, y)


# Create a MLflow experiment named "ml-monitoring"
mlflow.set_experiment("ml-monitoring")

# Start a new MLflow run - context manager handles start/end
with mlflow.start_run():
    mlflow.log_metric("accuracy", accuracy) # Log accuracy metric to MLflow
    mlflow.sklearn.log_model(model, "model") # Save/log trained model in MLflow

joblib.dump(model, "model/latest_model.pkl") # Save the trained model locally as a .pkl file

print("Model tained. Accuracy:", accuracy)