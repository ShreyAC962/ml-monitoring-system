import mlflow 
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("data/sample_stream.csv") # load from csv file to DataFrame
X = df.drop("label", axis = 1) # Remove target column "label"

# Predict - Target variable
y = df["label"]

# Splitting into training and testing
X_train, X_test, y_train, y_test = train_test_split(X,y)

model = RandomForestClassifier()

# Training the model using training data
model.fit(X_train, y_train)

# Evaluate model performance on test data - returns accuracy
accuracy = model.score(X_test, y_test)

# Start an MLflow experiment run
mlflow.start_run()

# Log the accuracy metric to MLflow
mlflow.log_metric("accuracy", accuracy)

# Save the log of trained model in MLflow
mlflow.sklearn.log_model(model, "model")

# End the Mlflow run
mlflow.end_run()
