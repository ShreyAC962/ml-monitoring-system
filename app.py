from services.circuit_breaker import check_model_health
from services.rollback import rollback_to_best
from services.retrain import retrain
from monitoring.metrics import update_metrics


def main_loop():
    accuracy = 0.7
    drift = True
    update_metrics(accuracy, drift)

    if check_model_health(accuracy, drift):
        print("Triggering Circuit Breaker")

        rollback_to_best() # Roll back to the best performing model from MLflow

        retrain() # Trigger retraining of a new model


if __name__ == "__main__":
    main_loop()

    


