import mlflow 
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib # To save/load trained models
import pandas as pd
import time

def train_model(data_path="data/sample_stream.json"):

    df = pd.read_json(data_path) # laod data from a JSON file into a DataFrame

    X = df[["feature1", "feature2"]] # input features - independent variables
    y = df["label"] # target variable - what we want to predict

    X_train, X_test, y_train, y_test = train_test_split(X,y)

    model = RandomForestClassifier(n_estimators=100)

    # Train the model using training data
    model.fit(X_train, y_train)

    # Evaluate model performance on test data
    accuracy = model.score(X_test, y_test)  

    version = str(int(time.time())) # Create unique version using current timestamp


    # Create a MLflow experiment named "ml-monitoring"
    mlflow.set_experiment("ml-monitoring")

    # Start a new MLflow run - context manager handles start/end
    with mlflow.start_run():
        mlflow.log_metric("accuracy", accuracy) # Log accuracy metric to MLflow
        mlflow.log_param("version", version) # Log model version as a parameter
        mlflow.sklearn.log_model(model, "model") # Save/log trained model in MLflow

    
    joblib.dump(model, f"model/candidate_model_{version}.pkl")   # Save model locally as a candidate version

    print(f"[TRAIN] Model trained | Accuracy: {accuracy} | Version: {version}")  # Print training status
    return accuracy, version, model     # Return results for further pipeline use
