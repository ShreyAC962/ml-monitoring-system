import os
import joblib
from model.train import train_model
from services.rollback import promote_model # Import function that promotes a model to production (golden model)

def retrain_model(trigger_reason="drift_detected"):
    print("Retraining triggered due to:", trigger_reason)

    # Step 1: Train new model
    accuracy, version, model = train_model()

    print(f"New model trained: v{version}, accuracy={accuracy}")

    # Step 2: Load current best model accuracy
    current_best_path = "model/golden_model.pkl"

    if os.path.exists(current_best_path):
        print("Found existing Golden Model")
    else:
        print("No golden model found. Promoting first model")
        promote_model(version, model)
        return

    # Step 3: Compare models (simple logic here)
    # In real systems: fetch from MLflow registry
    if accuracy > 0.75:
        print("New model is better → promoting")
        promote_model(version, model)
    else:
        print("New model not better → rejected")