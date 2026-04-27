import joblib
import os

def promote_model(version, model):
    path = "model/golden_model.pkl"

    joblib.dump(model, path) # Save the trained model to disk as the golden model

    print(f"New GOLDEN MODEL promoted: version={version}")  


def rollback_to_best():
    path = "model/golden_model.pkl" 
    if os.path.exists(path):
        print("Rolling back to last GOLDEN model")
        return joblib.load(path)
    else:
        print("No golden model available")
        return None



